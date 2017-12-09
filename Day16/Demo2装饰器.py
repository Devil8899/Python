#_author: liuz
#date: 2017/12/9


#学习装饰器函数

#开放  封闭原则   对修改源码封闭  对扩展源码开放
#函数名加括号就是执行函数，没加就是函数内存地址就可以了
import time

#装饰器函数
def showtime(timefun):     #对函数做了封装
    def inner():           #闭包   内部函数+要使用外部环境变量
        start = time.time()
        timefun()
        end = time.time()
        show = end - start
        print('函数执行时间%s' % show)
    return inner
#想通过time1()方法调用    不修改调用方式
#time1=showtime(time1)   #这里执行的就是inner()方法
#time1()

#python提供了装饰器的写法  更加简单 @装饰器方法名 等于了这句话  time1=showtime(time1)
@showtime
def time1():              #功能函数
    time.sleep(1)
    print("this time1")

@showtime
def time2():
    time.sleep(2)
    print("this time2")

time1()  #是执行了inner函数  同时把time1方法作为参数传入 在inner函数内执行


#showtime(time2)         #将函数名作为参数传入


