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


import select


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
