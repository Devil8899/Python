#_author: liuz
#date: 2017/12/18
import os
'''
python中的反射功能是由以下四个内置函数提供：hasattr、getattr、setattr、delattr，
四个函数分别用于对对象内部执行：检查是否含有某成员、获取成员、设置成员、删除成员。
'''
import test

class Foo(object):
    def __init__(self):
        self.name = 'test'

    def func(self):
        return 'func'

    def showmsg(self):
        print("showmsg")
obj = Foo()

# #### 检查是否含有成员 ####
r=hasattr(obj, 'name')
r2=hasattr(obj, 'func')
print(r,r2)
# #### 获取成员 ####
r3=getattr(obj, 'name')
r4=getattr(obj, 'func')
print(r3)
# #### 设置成员 ####
setattr(obj, 'age', 18)
setattr(obj, 'show', lambda num: num + 1)
print(obj.show(1))
# #### 删除成员 ####
#print(delattr(obj,'name'))
#print(delattr(obj,'showmsg'))


#反射也可以是是模块内的属性和方法或者是类
print(getattr(test,'NAME'))
con=getattr(test,'testclass')  #返回模块中的类
print(con.age)