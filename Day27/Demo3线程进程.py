#_author: liuz
#date: 2017/12/19

import threading,time  #线程模块
'''
1.多任务可以由多进程完成，也可以由一个进程内的多线程完成。
2.进程是由若干线程组成的，一个进程至少有一个线程。
3.由于线程是操作系统直接支持的执行单元，因此,高级语言通常都内置多线程的支持，Python也不例外，
4.并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。
5.Python的标准库提供了两个模块：thread和threading，thread是低级模块，threading是高级模块，对thread进行了封装。
6.绝大多数情况下，我们只需要使用threading这个高级模块。
7.启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
'''
start=time.time()
#主线程
def test(n):
    time.sleep(5)
    print("%s"%n)
    print(threading.current_thread().name)   #获取执行的线程名字
def test2(n):
    time.sleep(5)
    # print("%s"%n)
    print(threading.current_thread().name)   #获取执行的线程名字

#创建子线程对象  传入一个函数
thr=threading.Thread(target=test2,args=('test',),name='LoopThread') #如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
thr2=threading.Thread(target=test2,args=('test',),name='LoopThread2') #如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
# test(1)
#运行线程
thr.start()
thr2.start()
thr.join()
thr2.join()
end=time.time()
print('start in main')
print(end-start)