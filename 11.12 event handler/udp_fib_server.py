import socket
import time
import os
import select
from concurrent.futures import ThreadPoolExecutor


def event_loop(handlers):
    handlers: list[EventHandler]
    while True:
        wants_recv = [h for h in handlers if h.wants_to_receive()]
        wants_send = [h for h in handlers if h.wants_to_send()]

        can_recv, can_send, _ = select.select(wants_recv, wants_send, [])
        for h in can_recv:
            h.handle_receive()
        for h in can_send:
            h.handle_send()


class EventHandler:
    def fileno(self):
        """返回联合文件描述符"""
        raise NotImplemented("must implement")

    def wants_to_receive(self):
        """return True if receiving is allowed"""
        return False

    def handle_receive(self):
        """perform the receive operation"""
        pass

    def wants_to_send(self):
        """return True if sending is requested"""
        return False

    def handle_send(self):
        """send outgoing data"""
        pass


class ThreadPoolHandler(EventHandler):
    def __init__(self, nworkers):
        if os.name == "posix":
            self.signal_done_sock, self.done_sock = socket.socketpair()
        else:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(("127.0.0.", 0))
            server.listen(1)
            self.signal_done_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.signal_done_sock.connect(server.getsockname())
            self.done_sock, _ = server.accept()
            server.close()

        self.pending = []
        self.pool = ThreadPoolExecutor(nworkers)

    def fileno(self):
        return self.done_sock.fileno()

    def _complete(self, callback, r):
        """当线程结束时回调这个"""
        self.pending.append((callback, r.result()))
        self.signal_done_sock.send(b"x")

    def run(self, func, args=(), kwargs=None, *, callback):
        """在一个线程中执行func"""
        if kwargs is None:
            kwargs = {}
        r = self.pool.submit(func, *args, **kwargs)
        r.add_done_callback(lambda r: self._complete(callback, r))

    def wants_to_receive(self):
        return True

    def handle_receive(self):
        """执行回调函数在完成工作后"""
        for callback, result in self.pending:
            callback(result)
            self.done_sock.recv(1)
        self.pending = []


class UDPServer(EventHandler):
    def __init__(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(address)

    def fileno(self):
        return self.sock.fileno()

    def wants_to_receive(self):
        return True


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


class UDPFibServer(UDPServer):
    def handle_receive(self):
        msg, addr = self.sock.recvfrom(128)
        n = int(msg)
        pool.run(fib, (n,), callback=lambda r: self.respond(r, addr))

    def respond(self, result, addr):
        self.sock.sendto(str(result).encode("ascii"), addr)


if __name__ == '__main__':
    pool = ThreadPoolHandler(16)
    handlers = [pool, UDPFibServer(("", 16000))]
    event_loop(handlers)
