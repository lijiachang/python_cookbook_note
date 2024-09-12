import hmac
import os


def client_authenticate(connection, secret_key):
    msg = connection.recv(32)

    # 客户端和服务器通过 hmac 模块以及双方事先都知道的密钥计算出随机数据的加密 hash。
    digestmod = "sha1"  # python 3.8+ 需要提供加密算法，比如说MD5、sha1
    hash_ = hmac.new(secret_key, msg, digestmod)
    digest = hash_.digest()

    connection.send(digest)  # 发送摘要


def server_authenticate(connection, secret_key):
    msg = os.urandom(32)  # 返回一个适合加密使用的随机字节串
    connection.send(msg)

    # 客户端和服务器通过 hmac 模块以及双方事先都知道的密钥计算出随机数据的加密 hash。
    digestmod = "sha1"  # python 3.8+ 需要提供加密算法，比如说MD5、sha1
    hash_ = hmac.new(secret_key, msg, digestmod)
    digest = hash_.digest()

    response = connection.recv(len(digest))  # 接收摘要

    return hmac.compare_digest(digest, response)  # 对只要值进行比较。然后决定接收还是拒绝这个连接


from socket import socket, AF_INET, SOCK_STREAM

secret_key = b'key123'


def echo_handler(client_sock):
    if not server_authenticate(client_sock, secret_key):
        client_sock.close()
        return

    while True:
        msg = client_sock.recv(8192)
        if not msg:
            break
        client_sock.sendall(msg)


def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)

    while True:
        c, a = s.accept()
        echo_handler(c)


echo_server(('', 18000))
