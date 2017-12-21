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