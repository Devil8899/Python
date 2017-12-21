#_author: liuz
#date: 2017/12/21
from multiprocessing import Process
import time

#创建一个类
class myProcess(Process):
    def __init__(self):
        # Process.__init__()
        super(myProcess,self).__init__()
    def run(self):           #重写run方法
        time.sleep(1)
        print(self.name)


if __name__=="__main__":
    list_pro=[]
    for i in range(3):
        t=myProcess()
        t.start()
        list_pro.append(t)

    for p in list_pro:
         p.join()
    print("主进程。。。")