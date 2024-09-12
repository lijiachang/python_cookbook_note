from socketserver import StreamRequestHandler, TCPServer

class EchoHandler(StreamRequestHandler):
    def handle(self):
        # self.rfile 能读取文件流
        for line in self.rfile:
            # self.wfile 能写文件流
            self.wfile.write(line)

if __name__ == '__main__':
    from threading import Thread
    WORKERS = 16
    serv = TCPServer(('', 20000), EchoHandler)
    for n in range(WORKERS):
        t = Thread(target=serv.serve_forever)
        t.daemon = True
        t.start()
    serv.serve_forever()