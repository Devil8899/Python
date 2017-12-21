#_author: liuz
#date: 2017/12/20

import threading,time
'''自定义线程类
1.继承threading.Thread
2.调用父类的构造函数
3.重写run方法
4.实例化对象开启线程
'''

class mythred(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):          #开启线程要运行的函数
        time.sleep(3)
        print("123",self.num)

if __name__=='__main__':
    t1=mythred()   #创建一个实例化线程对象
    t1.num=3
    t2=mythred()
    t2.num=3

    t1.start()
    t2.start()
