#_author: liuz
#date: 2017/12/21’
import time
from multiprocessing import Process,Pipe,Queue #进程队列类Queue
'''
进程之间的数据共享和通信  进程间通信是通过Queue、Pipes等实现的。
1.主进程和子进程数据通信

'''
#id() 函数用于获取对象的内存地址。

#第一种通过队列
'''
def DataQ(q):
    q.put([1,2,3])
    print('children q id',id(q))

if __name__=="__main__":
    q=Queue()     # 父进程创建Queue，并传给各个子进程：
    P_list=[]
    q.put("123")
    print('main q id',id(q))
    for i in range(3):
        pro=Process(target=DataQ,args=(q,))  #将主进程创建好的队列作为参数传入
        pro.start()
    #主进程获取改变后的数据  但是q是不同的内存地址 这里数据应该是复制了一份给了主进程
    print(q.get())
    print(q.get())
    print(q.get())

'''
#第二种通过过Pipe
#Pipe类似与socket通信  一个服务端 一个客户端  是一个管道通信
def Datab(conn):
    age=20
    conn.send({'name':'jerry','age':age})  #给主进程发送一个数据
    print(conn.recv())                     #接收


if __name__=="__main__":
    parent_conn,children__conn=Pipe()   #实例化类  拿到2个对象  个服务端 一个客户端
    p=Process(target=Datab,args=(children__conn,))
    p.start()
    print(parent_conn.recv())  #主进程接收数据
    parent_conn.send((1,2,3))  #发送给子进程
    time.sleep(1)
    p.join()
    print("主进程执行完成。。。")