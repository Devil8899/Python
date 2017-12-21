#_author: liuz
#date: 2017/12/21

from multiprocessing import Process
import  time,os
'''
每个进程都有一个父进程

'''
def info(title):
    print(title)
    print('module_name',__name__)
    print('parent_process',os.getppid()) #父进程运行进程号 如果在编译器下运行 这个就是pycharme
    print('process id',os.getpid())      #当前运行进程号

def f(name):
    print("")

if __name__=="__main__":
    info('parent')
    time.sleep(10)
    p=Process(target=info,args=('children',))
    p.start()
    p.join()