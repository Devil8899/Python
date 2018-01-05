#_author: liuz
#date: 2018/1/5
from wsgiref.simple_server import make_server
from urls import  routers
def application(environ, start_response):

    print(environ['PATH_INFO'])
    path=environ['PATH_INFO']
    start_response('200 OK', [('Content-Type', 'text/html')])
    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if item[0] == path:
            func = item[1]
            break
    if func:
        return func(environ)
    else:
        return ["<h1>404</h1>".encode("utf8")]

httpd = make_server('', 8518, application)

print('Serving HTTP on port 8084...')

# 开始监听HTTP请求:

httpd.serve_forever()