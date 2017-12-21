#_author: liuz
#date: 2017/12/20
import time,threading
#IO密集型函数
#计算密集型函数
'''
join的作用是保证当前线程执行完成后，再执行其它线程
join可以有timeout参数，表示阻塞其它线程timeout秒后，不再阻塞
1.join方法的作用是阻塞主进程（挡住，无法执行join以后的语句），专注执行多线程。
2.多线程多join的情况下，依次执行各线程的join方法，前头一个结束了才能执行后面一个。
3.无参数，则等待到该线程结束，才开始执行下一个线程的join。
4.设置参数后，则等待该线程这么长时间就不管它了（而该线程并没有结束）。不管的意思就是可以执行后面的主进程了。
5.逐个执行每个线程，执行完毕后继续往下执行，该方法使得多线程变得无意义
'''
start=time.time()
def add(n):
    sum=0
    for i in range(n):
        sum+=i

#add(100000000)
#add(200000000)
thr1=threading.Thread(target=add,args=(100000000,))
thr2=threading.Thread(target=add,args=(200000000,))
thr1.start()
thr2.start()
thr1.join()
thr2.join()
end=time.time()
print(end-start)