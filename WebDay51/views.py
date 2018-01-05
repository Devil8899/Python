#_author: liuz
#date: 2018/1/5
import time

def f1(req):
    print(req)
    print(req["QUERY_STRING"])

    f1=open("index.html","rb")
    data1=f1.read()
    return [data1]

def f2(req):

    f2=open("index2.html","rb")
    data2=f2.read()
    return [data2]


def f3(req):        #模版以及数据库

    f3=open("index3.html","rb")
    data3=f3.read()
    times=time.strftime("%Y-%m-%d %X", time.localtime())
    data3=str(data3,"utf8").replace("!time!",str(times))
    return [data3.encode("utf8")]
