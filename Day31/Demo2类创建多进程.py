#_author: liuz
#date: 2017/12/21
from multiprocessing import Process
import time

#创建一个类 继承进程类
class myProcess(Process):
    def __init__(self):
        # Process.__init__()
        super(myProcess,self).__init__()  #调用父类的构造函数
    def run(self):                       #重写run方法
        time.sleep(1)
        print(self.name)


if __name__=="__main__":
    list_pro=[]
    for i in range(3):
        t=myProcess()           #创建3个进程
        t.start()               #开启进程
        list_pro.append(t)      #加入列表

    for p in list_pro:
         p.join()
    print("主进程。。。")