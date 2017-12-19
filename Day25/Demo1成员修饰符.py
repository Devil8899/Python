#_author: liuz
#date: 2017/12/17
import os
'''
1.私有字段 无论是类字段或者成员字段 都不能外部直接访问
2.私有方法 无论进静态方法或者内部方法 都不能直接访问
3.私有字段或方法都不能继承给子类使用

关于构造函数：如果在子类中没有构造函数 解释器会从子类的父类开始执行构造函数
如果子类存在 则不会执行父类构造函数
'''

class people:
    Work='driver'
    #私有类字段
    __work2='driver'
    def __init__(self,name):
        self.__age=20           #定义私有字段
        self.name=name
    def getage(self):          #类内部访问私有字段
        return self.__age
    #私有方法
    def __getage2(self):
        return  "123"+people.__work2
    def getLoage(self):
        print(self.__getage2()) #类内部访问私有方法

    #静态方法
    @staticmethod
    def getmsg():
        print("静态方法")

doctor=people('jerry')
doctor.name
#doctor.__age                    #不能直接访问
#print(doctor.getage())
#doctor.__getage2()              #私有方法不能直接访问
doctor.getLoage()
#doctor.__Work
#people.getmsg()


class son(people):
        def __init__(self):
            pass
s1=son()
print(s1.Work)
#print(s1.__age)