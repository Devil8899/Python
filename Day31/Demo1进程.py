#_author: liuz
#date: 2017/12/21


from multiprocessing import Process
import os
'''
multiprocessing模块提供了一个Process类来代表一个进程对象
多进程
创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，
用start()方法启动，这样创建进程比fork()还要简单。
在linux/mac中可以使用fork()创建
'''
# 子进程要执行的代码

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())     #运行此句的进程号 主进程
    p = Process(target=run_proc, args=('test',))  #创建子进程实例
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')


