#_author: liuz
#date: 2017/12/21
import os
'''
协程
1.一个线程处理
但协程的特点在于是一个线程执行，那和多线程比，协程有何优势？
最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，
而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，
协程的性能优势就越明显。
第二大优势就是不需要多线程的锁机制，因为只有一个线程，
也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，
所以执行效率比多线程高很多。
因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，
既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
Python对协程的支持是通过generator(生成器对象yield)实现的。
yield 造成的一种并发的效果
'''

def Cus_generator(name):
    print("------>car start------>")
    while True:
        my_car=yield
        print("[%s] starting [%s]"% (name,my_car))

def producer():
    next(con)
    next(con1)
    n=0
    while n<5:
       n+=1
       con.send(n)   #next 同时设置值  执行从yield开始
       con1.send(n)
       print("car_______________________________end")


if __name__=="__main__":
    con=Cus_generator('BMW')    #创建一个生成器对象
    con1=Cus_generator('AuDi')
    producer()
