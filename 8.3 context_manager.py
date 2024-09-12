from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:
    def __init__(self, address, family=AF_INET, type_=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type_
        self.socket = None

    def __enter__(self):
        if self.socket is not None:
            raise RuntimeError('Already connected')

        self.socket = socket(self.family, self.type)
        self.socket.connect(self.address)
        return self.socket

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.socket.close()
        self.socket = None


from functools import partial

conn = LazyConnection(('www.python.org', 80))
# connection closed.
with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')

    resp = b''.join(iter(partial(s.recv, 8192), b''))  # iter一直迭代接收，直到返回b''为止
    print(resp)
    raise Exception(123)
    # conn.__exit__() executes: connection close


