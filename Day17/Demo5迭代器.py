#_author: liuz
#date: 2017/12/11


#学习 生成器都是迭代器  迭代器不一定是生成器
#list,tuple,dict,string(可迭代对象)

#什么是迭代器
#满足2个条件:1.有iter方法 2.有next方法


lo=[1,2,3]
d=iter(lo)       #等价于 lo.__iter__()   iter()将迭代对象转换为迭代器
#print(d)         #<list_iterator object at 0x0000021EE4CAD160>

#print(next(d))  #1

#for循环内部三件事：
#1.调用可迭代对象的iter方法 返回一个迭代器对象
#2.不断调用迭代器对象的Next方法
#3.处理异常
'''
for i in [1,2,3]:
    print(i)
'''

#Iterator 迭代器
#Iterable 可迭代对象

#isinstance  判断对象类型
from collections import Iterator,Iterable
#print(isinstance([1,2],list))
#print(isinstance('string',str))
print(isinstance(lo,list))
print(isinstance(lo,Iterable))  #迭代对象   True
print(isinstance(lo,Iterator))  #迭代器     False
#可以使用isinstance()判断一个对象是否是Iterable对象：

'''
总结：
凡是可作用于for循环的对象都是Iterable可迭代对象类型；
凡是可作用于next()函数的对象都是Iterator迭代器类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
'''