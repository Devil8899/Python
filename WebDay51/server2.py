#_author: liuz
#date: 2018/1/4



from wsgiref.simple_server import make_server
import time
'''
使用Web Server Gateway Interface建立一个web服务端
'''

def application(environ, start_response):
    #environ 封装所有请求头信息
    # start_response设置响应头 更easy的设置,自己手写socketweb服务器更方便 这就是WSGIServer和socket做一个对比
    start_response('200 OK', [('Content-Type', 'text/html')])
    with open('index.html','rb')as f:
        data=f.read()
        data=str(data,'utf8').replace('time',str(time.ctime()))
    return [data.encode('utf8')]
    # if environ["PATH_INFO"]=="/book":
    #     return [b'<h1>Hello, bookpage!</h1>']  # 返回给客户端的页面
    # elif environ["PATH_INFO"]=="/web":
    #     return [b'<h1>Hello, webroot!</h1>']  # 返回给客户端的页面
    # else:
    #     return [b'<h1>404</h1>']  # 返回给客户端的页面

#引入simple_server模块 调用了make_server方法
#返回一个WSGIServer服务器
httpd = make_server('', 8002, application)

print('Serving HTTP on port 8002...')
# 开始监听HTTP请求:等待连接
httpd.serve_forever()

'''
def f1(req):
    print(req)
    print(req["QUERY_STRING"])

    f1=open("index1.html","rb")
    data1=f1.read()
    return [data1]

def f2(req):

    f2=open("index2.html","rb")
    data2=f2.read()
    return [data2]

import time

def f3(req):        #模版以及数据库

    f3=open("index3.html","rb")
    data3=f3.read()
    times=time.strftime("%Y-%m-%d %X", time.localtime())
    data3=str(data3,"utf8").replace("!time!",str(times))
    return [data3.encode("utf8")]


def routers():
    urlpatterns = (
        ('/yuan',f1),
        ('/alex',f2),
        ("/cur_time",f3)
    )
    return urlpatterns


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
'''