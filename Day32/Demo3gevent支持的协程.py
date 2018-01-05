#_author: liuz
#date: 2017/12/21
import gevent,time
#1.安装库gevent
'''
Python通过yield提供了对协程的基本支持，但是不完全。
而第三方的gevent为Python提供了比较完善的协程支持。
gevent是第三方库，通过greenlet实现协程，其基本思想是：

当一个greenlet遇到IO操作时，比如访问网络
，就自动切换到其他的greenlet，
等到IO操作完成，再在适当的时候切换回来继续执行
。由于IO操作非常耗时，经常使程序处于等待状态
，有了gevent为我们自动切换协程，就保证总有greenlet在运行，
而不是等待IO。
'''
start=time.time()
def test1():
   print("12")
   gevent.sleep(1)  #sleep方法模拟io阻塞
   #遇到IO操作执行进行下一个gevent任务
   print("56")
def test2():
   print("34")
   gevent.sleep(2)
   print('78')
gevent.joinall([
    gevent.spawn(test1),
    gevent.spawn(test2)
])
print(time.time()-start)