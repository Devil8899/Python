#_author: liuz
#date: 2017/12/11

#列表生成式

d=[x for x in range(1,10)]
#print(d)

#生成器
#1.创建生成器2种方式  generator object
w=(x*2 for x in range(10))
#print(w)            #w就是一个生成器
#2.yield关键字
def genera():
    print("ok")
    count=yield 1
    print(count)
    print("msg2")
    yield 2
#genera()           就是一个生成器


#2.生成器方法
#next(genera())   #计算一个值

#遍历所有元素可以通过for循环
'''
for i in [1,2,3]:
   print(i)
'''
#for循环内部三件事：
#1.调用可迭代对象的iter方法 返回一个迭代器对象
#2.不断调用迭代器对象的Next方法
#3.处理异常

#send方法  有next()功能同时 并且给变量赋值
b=genera()
next(b)
b.send('eee')


#迭代器协议
# 生成器都是迭代器  迭代器不一定是生成器
#1.内部有next()方法  2.内部有iter()方法
