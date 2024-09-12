from socketserver import StreamRequestHandler, TCPServer
import functools


class EchoHandler(StreamRequestHandler):
    def __init__(self, *args, ack, **kwargs):  # 注意这里在*args后面是ack是仅限关键字参数
        self.ack = ack
        super().__init__(*args, **kwargs)

    def handle(self) -> None:
        for line in self.rfile:
            self.wfile.write(self.ack + line)


# 是用partial解决参数问题
server = TCPServer(('', 15000), functools.partial(EchoHandler, ack=b'RECEIVED'))
server.serve_forever()
