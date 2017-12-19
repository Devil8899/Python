#_author: liuz
#date: 2017/12/17
import os
'''
        __init__  构造方法  创建对象自动调用
        __call__  对象() 或者 类名()() 自动调用
        __int__   在使用int(对象)转换时会自动调用该对象内部的__int__方法
        __str__   1.如果构造函数给字段赋值有字符串时调用或者在str(对象)转换使用时会自动调用对象的__str__方法
        __add__   对象相加时自动调用
        __del__   python自动调用  对象被销毁时
        __dict__  通过字典形式将对象成员显示出来  实例化对象调用
        通过索引的方式给对象赋值取值  通过切片一样会调用这些方法
        __getitem__
        __setitem__
        __delitem__
        __iter__    类里面是有__iter__()代表可迭代对象 
         当对象执行迭代方法时会自动调用此方法返回一个迭代器对象 再对迭代器对象
         执行next()方法
'''
#类的特殊成员
class dog:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __call__(self, *args, **kwargs):
        print("调用call方法")

    def __int__(self):
        print("在int转换时调用")
        return 8
    def __str__(self):
        print("在str转换时调用")
        return "9"
    #对象相加时会调用
    def __add__(self, other):
        #self =d('tom',20)
        #other=d2('jerry',30)
        print(self.name,other.name)
        return 1
    #析构方法
    # def __del__(self):
    #    print("析构方法 对象被销毁时自动执行  python内部执行")
    #__dict__调用

    #根据索引取值
    def __getitem__(self, item):   #slice(1, 4, 2) <class 'slice'>
       # return item+10
       print(item,type(item))
    #给索引赋值
    def __setitem__(self, key, value): #key=3  value=100
        print(key,value)
    #删除值
    def __delitem__(self, key):
        print(key)

    #切面形式同样会调用__getitem(self,item)
    def __getitem__(self, item):  #item封装了3个值
         #判断是不是切片类型
         if type(item)==slice:      #slice对象有三个属性  有了属性后 自己就可以写逻辑
            print(item.start)              #起始位置
            print(item.stop)                #结束位置
            print(item.step)                #步长
            print("做切片处理")
         else:
             print("索引处理")
    #当在循环中调用可迭代对象的iter方法 返回一个迭代器对象
    def __iter__(self):
            return iter([1,2,3])
print("______________________________________________________________________")
d=dog('tom',20)
d()  #调用call()
str1=str(d)
int1=int(d)

d2=dog('jack',30)
print(d+d2)
#当两个对象相加时会自动调用第一个对象中的__add()__方法,并将第2个对象作为参数传入

print(d2.__dict__)#通过字典形式  {'age': 30, 'name': 'jack'}

print("_____________________下面代码之间和方法都是一个对应关系可以在方法里面自己写逻辑______________________________")
#规定这种语法 它会自动执行python里面的方法
r=d2[2]  #[索引]形式会自动调用类中的__getitem()方法  2作为参数传给item
d2[3]=100#赋值操作自动调用__setitem()方法
del d2[3]#自动执行__deltitem()方法

#切片对应的方法 __getitem__  切片也可以写赋值  删除值操作等等
d2[1:4:2]      #会传一个对象到方法中 Slice  $slice(1, 4, 2) <class 'slice'>
#d2[1:4]=[1,2]  #赋值操作自动调用__setitem

'''
                # 如果类中有 __iter__ 方法，对象=》可迭代对象
                # 对象.__iter__() 的返回值： 迭代器
                # for 循环，迭代器，next
                # for 循环，可迭代对象，对象.__iter__()，迭代器，next
                # 1、执行li对象的类F类中的 __iter__方法，并获取其返回值
                # 2、循环上一步中返回的对象
'''
for i in d2:
    print(i)