#_author: liuz
#date: 2017/12/9


#定义装饰器函数   功能函数无参数
'''
def allNews(newfun):
    def inner():
        newfun()
        print("newsall")
    return inner

@allNews
def showNew1():
    print("new1")

def showNew2():
    print("new2")

showNew1()
'''


#带参数的装饰器函数  不定长参数

def allNews(newfun):
    def inner(*a):
        newfun(a)
        print("newsall")
    return inner

#功能函数加参数
@allNews
def showNew1(*args):  #showNew1=allNews(showNew1)
    print(args)
    print("new1")

def showNew2(*a):
    sum=0
    for i in a:
         sum+=i
    print(sum)
    print("new2")

#showNew2(1,2,3) #调用inner方法 inner方法内部再执行showNew1方法完成计算 打印


#带参数的装饰器函数
def loger(log=''):
    def logerfun(loger):
        def logerW():
            loger()
            if log=="true":               #因为是闭包所以能调用到外部变量log
                print('写入日志成功')
        return logerW
    return logerfun


#调用的装饰器函数含参数 调用时直接传值
#loger1=loger('true')
#loger1=logerfun(loger1)
@loger('true')
def loger1():
    print('logerwrite1')

@loger('false')
def loger2():
    print('logerwrite2')

loger2()