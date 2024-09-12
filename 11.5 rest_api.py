import cgi


def notfound_404(environ, start_response):
    start_response("404 Not Found", [("Content-type", "text/plain")])
    return [b"Not Found"]


class PathDispatcher:
    def __init__(self):
        self.pathmap = {}

    def __call__(self, environ, start_response, *args, **kwargs):
        # 参数 environ 是一个字典，其中需要包含的值参考了许多 Web 服务器比如 Apache 所提 供的 CGI 接口的启发
        path = environ['PATH_INFO'] # 请求资源的路径
        params = cgi.FieldStorage(environ['wsgi.input'],
                                  environ=environ)
        method = environ['REQUEST_METHOD'].lower() # 表示请求的类型(例如 GET、POST、HEAD 等)
        environ['params'] = {key: params.getvalue(key) for key in params}
        header = self.pathmap.get((method, path), notfound_404)
        return header(environ, start_response)

    def register(self, method, path, function):
        self.pathmap[method.lower(), path] = function
        return function

import time

_hello_resp = '''<html>
<head>
<title>Hello {name}</title>
</head> <body>
<h1>Hello {name}!</h1> </body>
</html>'''

def hello_world(environ, start_response):
    # 参数 start_response 是一个函数，必须调用它才能发起响应。start_response 的第一个参 数是 HTTP 结果状态。
    # 第二个参数是一个元组序列，以(name, value)这样的形式组成响 应的 HTTP 头。
    start_response("200 OK", [("Content-type", "text/html",)])
    params = environ['params']
    resp = _hello_resp.format(name=params.get('name'))
    # 要返回数据，满足 WSGI 规范的应用程序必须返回字节串序列
    yield resp.encode('utf-8')

_localtime_resp = '''<?xml version="1.0"?> 
<time>
    <year>{t.tm_year}</year> 
    <month>{t.tm_mon}</month> 
    <day>{t.tm_mday}</day> 
    <hour>{t.tm_hour}</hour> 
    <minute>{t.tm_min}</minute> 
    <second>{t.tm_sec}</second>
</time>'''

def localtime(environ, start_response):
    start_response('200 OK', [('Content-type', 'application/xml',)])
    resp = _localtime_resp.format(t=time.localtime())
    yield resp.encode('utf-8')

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    dispatcher = PathDispatcher()
    dispatcher.register("GET", '/hello', hello_world)
    dispatcher.register('GET', '/localtime', localtime)

    httpd = make_server('', 8080, dispatcher)
    print('serving on port 8080')
    httpd.serve_forever()
