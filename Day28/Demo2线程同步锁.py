#_author: liuz
#date: 2017/12/20
import threading,time
'''
线程锁：
   Lock
   而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改
   ，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。     
'''
r=threading.Lock()       #1.创建一个线程锁对象
def changeNum():
    global num
    r.acquire()           #2.加锁  当锁内部代码执行完成后 cpu释放资源给下一个线程执行
    tmp=num
    time.sleep(0.1)
    num=tmp-1
    r.release()         #3.释放锁
    # num -= 5
    # print(threading.current_thread().name, num)
#全局变量
num=100

thread_list=[]

for i in range(100):
    t1 = threading.Thread(target=changeNum,name='男人')
    # t2 = threading.Thread(target=changeNum,name='女人')
    t1.start()
    # t2.start()
    thread_list.append(t1)

for t in thread_list:  #等待所有线程执行完毕后 再执行主线程
    t.join()

print('final num',num)
'''
锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，
首先是阻止了多线程并发执行(被执行锁的代码只能串行一个一个线程执行)
，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。
其次，由于可以存在多个锁，不同的线程持有不同的锁，
并试图获取对方持有的锁时，
可能会造成死锁，导致多个线程全部挂起，
既不能执行，也无法结束，只能靠操作系统强制终止。
'''