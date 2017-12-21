#_author: liuz
#date: 2017/12/21
# from gevent import monkey
# monkey.patch_all()
import  gevent,time

from urllib.request import urlopen



'''
使用协程爬取网站
'''
def f(url):
    print("Get:%s"%url)
    resp=urlopen(url)
    data=resp.read()
    file=open('index.html','wb')
    file.write(data)
    print("%d bytes received from %s"%(len(data),url))

l=['http://www.python.org','http://www.zhihu.com','http://github.com']
start=time.time()
# for url in l:
#     f(url)

# f("http://www.xiaohuar.com/")

gevent.joinall([
    gevent.spawn(f,'http://www.python.org'),
    gevent.spawn(f,'http://www.zhihu.com'),
    gevent.spawn(f,'http://github.com')
])
#遇到IO阻塞自动切换
print(time.time()-start)
