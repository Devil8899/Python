#_author: liuz
#date: 2017/12/20

import threading,time
'''
信号量也是一把锁  :指同时开几个线程并发
Semaphore，是一种带计数的线程同步机制，当调用release时，增加计算
,当acquire时，减少计数，当计数为0时，自动阻塞，等待release被调用。
而在Python中存在两种Semphore，一种就是纯粹的Semphore，
还有一种就是BoundedSemaphore。
Semphore: 在调用release()函数时，不会检查，增加的计数是否超过上限（没有上限，会一直上升） 
BoundedSemaphore：在调用release()函数时，会检查，增加的计数是否超过上限，这样就保证了使用的计数
'''

import threading,time

class myThread(threading.Thread):
     def run(self):           #启动后，执行run方法
         if semaphore.acquire():  #加把锁，可以放进去多个（相当于5把锁，5个钥匙，同时有5个线程）
             print(self.name)
             time.sleep(5)
             semaphore.release()

if __name__=="__main__":
     semaphore=threading.Semaphore(5)  #同时能有几个线程进去（设置为5就是一次5个线程进去），类似于停车厂一次能停几辆车

     thrs=[] #空列表
     for i in range(100): #100个线程
        thrs.append(myThread()) #加线程对象

     for t in thrs:
         t.start()  #分别启动
'''
Semaphore是同时允许一定数量的线程更改数据，
比如车上有5个座位，那最多只允许5个人上车，后面的人只能等里面有人出来了才能再进去。
'''