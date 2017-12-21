#_author: liuz
#date: 2017/12/20

import threading,time
'''
信号量也是一把锁
Semaphore，是一种带计数的线程同步机制，当调用release时，增加计算
,当acquire时，减少计数，当计数为0时，自动阻塞，等待release被调用。
而在Python中存在两种Semphore，一种就是纯粹的Semphore，
还有一种就是BoundedSemaphore。
Semphore: 在调用release()函数时，不会检查，增加的计数是否超过上限（没有上限，会一直上升） 
BoundedSemaphore：在调用release()函数时，会检查，增加的计数是否超过上限，这样就保证了使用的计数
同时：
    在
'''

class mythread(threading.Thread):
    def run(self):
        # 获得信号量，信号量减一
       # seamp.acquire()
        seamp.acquire()
        print(self.name)
        time.sleep(1)
        # 释放信号量，信号量加一
        seamp.release()
        #seamp.release()  #ValueError: Semaphore released too many times



if __name__=='__main__':
    # 初始化信号量，数量为2，最多有2个线程获得信号量，信号量不能通过释放而大于2
    seamp=threading.BoundedSemaphore(10) #允许10个线程同时进入到锁内 但执行不是10个一起执行

threadlist=[]
#创建4个线程对象
for num in range(100):
    threadlist.append(mythread())
# 运行4个线程
for t in threadlist:
    t.start()
'''
Semaphore是同时允许一定数量的线程更改数据，
比如车上有5个座位，那最多只允许5个人上车，后面的人只能等里面有人出来了才能再进去。
'''