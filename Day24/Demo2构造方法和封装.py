#_author: liuz
#date: 2017/12/16

import  os
#构造方法   __init__()
#作用
#创建对象时自动执行
#给对象字段赋值  封装

class person:
    def __init__(self,name,age):          #"构造方法"
        #self=User1  nam3='tom',age=20
        self.name=name
        self.age=age
        #print(self.age)
    def eat(self):
        print(self.name,"在吃东西")

User1=person('tom',20)
User2=person('jerry',30)
User1.eat()
User2.eat()
'''
创建类  
    class person
        def eat():
            print('123')
    创建对象  boj=person()  同时调用构造方法
    调用方法  boj.eat()
    
构造方法  __init__(self)   self代表当前调用对象
    
封装    赋值
   __init__(self,name,age):
        self.name=name
        self.age=age
'''
