#_author: liuz
#date: 2017/12/20

import threading,time
'''
条件锁（threading.Condition）   默认是Rlock  
acquire  
release
使用线程等待，只有满足某条件时，才释放n个线程
acquire    给线程上锁
wait       wait方法释放当前线程占用的锁，同时挂起线程，直至被唤醒或超时（需timeout参数）。
当线程被唤醒并重新占有锁的时候，程序才会继续执行下去。
notify     条件创建后调用,通知等待池激活一个线程
notifyall  条件创建后,通知等待池激活所有线程
此方法不会释放锁定，使用前线程必须已获得锁定。否则将抛出异常
'''

import threading


def run(n):
    con.acquire()
    con.wait()
    print('run the thread:%s' % n)
    con.release()


if __name__ == '__main__':

    con = threading.Condition()  #创建一个对象
    for i in range(10):
        t = threading.Thread(target=run, args=(i,))
        t.start()

    while True:
        inp = input('>>>')
        if inp == 'q':
            break

        con.acquire()
        con.notifyAll()   #激活所有被阻塞的线程
        con.release()