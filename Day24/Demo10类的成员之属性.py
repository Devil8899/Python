#_author: liuz
#date: 2017/12/16
import os
'''
属性：@property   定义和方法无差别 也有返回值
                  调用时不用加（）
'''
class dog:
    def __init__(self,name):
        self.name=name
    def run(self):
        print("run fun")

    @property
    def eat(self):
        print("eat fun")

dog=dog('tom')
#dog.eat                #访问属性


#实际上属性是提供了我们访问字段和修改字段另一种方式

class cat :
    def __init__(self,name):
     self.name=name
     def eat(self):
        print("eat fun")

    @property
    def getname(self):
        return self.name

    @getname.setter
    def setname(self,val):
        self.name=val
    @getname.deleter
    def delname(self):
        del self.name

cat1=cat('tom')
cat1.setname='jerry'
del cat1.delname   #删除字段
print(cat1.getname)