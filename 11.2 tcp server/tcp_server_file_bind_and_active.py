import socket
from socketserver import StreamRequestHandler, TCPServer

class EchoHandler(StreamRequestHandler):
    # optional settings (defaults shown)
    timeout = 5
    rbufsize = -1 # read buffer size
    wbufsize = 0 #write buffer size
    disable_nagle_algorithm = False # sets TCP_NODELAY socket option
    def handle(self):
        print('got connection from', self.client_address)
        try:
            # self.rfile 能读取文件流
            for line in self.rfile:
                # self.wfile 能写文件流
                self.wfile.write(line)
        except socket.timeout:
            print('time out!')

if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler, bind_and_activate=False)

    # Set up various(各种各样） socket options
    serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # Bind and activate
    serv.server_bind()
    serv.server_activate()
    serv.serve_forever()

# 或者使用下面的方式
# if __name__ == '__main__':
#     TCPServer.allow_reuse_address = True
#     serv = TCPServer(('', 20000), EchoHandler)
#     serv.serve_forever()