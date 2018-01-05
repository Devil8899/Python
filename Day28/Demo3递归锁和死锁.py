#_author: liuz
#date: 2017/12/20

import threading,time
'''
1.死锁
2.递归锁  RLock()     一个锁对象   里面有一个  计数器

'''
class mythread(threading.Thread):

    def doa(self):
        lockc.acquire()
        print(self.name,'lock_a',time.ctime())
        time.sleep(3)
        lockc.acquire()
        print(self.name, 'lock_b', time.ctime())
        lockc.release()
        lockc.release()

    def dob(self):
        lockc.acquire()
        print(self.name, 'lock_b', time.ctime())
        time.sleep(3)
        lockc.acquire()
        print(self.name, 'lock_a', time.ctime())
        lockc.release()
        lockc.release()

    def run(self):
        self.doa()
        self.dob()

#locka=threading.Lock()
#lockb=threading.Lock()           #两把锁有可能会造成死锁现象
lockc=threading.RLock()           #递归锁   一把锁可以同时锁住和释放
threadslist=[]
for i in range(5):               #创建5个线程对象
    threadslist.append(mythread())

for t in threadslist:           #创建5个
    t.start()

'''同步锁和递归锁的区别
这两种琐的主要区别是：RLock允许在同一线程中被多次acquire锁住。而Lock同步锁却不允许这种情况。
注意：如果使用RLock，那么acquire和release必须成对出现，
即调用了n次acquire，必须调用n次的release才能真正释放所占用的琐。
'''