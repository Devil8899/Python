#_author: liuz
#date: 2017/12/8

#在python中内置了很多函数

#eval() 将字符串string对象转化为有效的表达式参与求值运算返回计算结果

print(eval('{"name":"jerry"}'))
print(eval('1+2*5'))


#filter(函数,序列) 过滤方法 循环遍历列表  有条件的过滤
def fun1(a):
    if a!='d':     #过滤d
        return  a

str=['a','b','c','d']
ret=filter(fun1,str)  #ret 返回一个迭代器  <filter object at 0x000002186FC57080>
print(list(ret)) #['a', 'b', 'c']  将迭代器转为一个list ['a', 'b', 'c']


#map(函数,序列)对序列做处理 比如拼接字符串
def fun2(a):
    return a+'hi'

ret2=map(fun2,str) #ret2 是一个迭代器对象
print(list(ret2))  #['ahi', 'bhi', 'chi', 'dhi']


#reduce(函数,序列) 返回是一个值 使用前需要加下面一句话
from _functools import reduce

def add1(x,y):
    return x + y

print(reduce(add1,[1,2,3,4,5]))#15


#lambda  匿名函数  无需定义函数名
add2=lambda a,b:a+b

print(add2(2,9))



