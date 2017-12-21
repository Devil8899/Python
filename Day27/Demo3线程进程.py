#_author: liuz
#date: 2017/12/19

import threading,time  #线程模块
'''代码自上而下执行
1.多任务可以由多进程完成，也可以由一个进程内的多线程完成。
2.进程是由若干线程组成的，一个进程至少有一个线程。
3.由于线程是操作系统直接支持的执行单元，因此,高级语言通常都内置多线程的支持，Python也不例外，
4.并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。
5.Python的标准库提供了两个模块：thread和threading，thread是低级模块，threading是高级模块，对thread进行了封装。
6.绝大多数情况下，我们只需要使用threading这个高级模块。
7.启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
'''
start=time.time()

def test(n):
    time.sleep(5)
    print(threading.current_thread().name)   #获取执行的线程名字
def test2(n):
    time.sleep(5)
    print(threading.current_thread().name)   #获取执行的线程名字

#创建2个子线程对象  传的两个参数第一个参数是，线程需要执行的方法，第二个参数方法的参数
thr=threading.Thread(target=test2,args=('test',),name='LoopThread') #如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
thr2=threading.Thread(target=test2,args=('test',),name='LoopThread2')
'''
function - 线程函数。
args - 传递给线程函数的参数,他必须是个tuple类型。
kwargs - 可选参数。
'''
test(1)
#运行线程
thr.start()
thr2.start()

#2个进程一块运行
thr.join()
thr2.join()

print('start in main')
end=time.time()
print(end-start)
'''
run(): 用以表示线程活动的方法,线程被cpu调度后执行Thread类对象的run方法
start():启动线程活动。
join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
isAlive(): 返回线程是否活动的。
getName(): 返回线程名。
setName(): 设置线程名。
setDaemon(True)  设置为后台线程或前台线程（默认）
如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，均停止
如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止
python中的多线程，有一个GIL（Global Interpreter Lock 全局解释器锁 ）
在同一时间只有一个线程在工作，他底层会自动进行上下文切换.这个线程执行点，那个线程执行点！
'''