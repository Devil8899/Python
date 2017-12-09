#_author: liuz
#date: 2017/12/8

#不定长 无参数名  传入元祖             1.直接传元祖/列表  2.正常调用
def PrintMsg(*args):
    print(args)
#PrintMsg([1,2,3]) #            ([1, 2, 3],)
#PrintMsg(*[1,2,3])  #         将列表传入  #(1, 2, 3)
#PrintMsg(*[1,2,3],*[4,5,6])#  (1, 2, 3, 4, 5, 6)
#PrintMsg(*(1,2,3)) #直接传元祖

#不定长  有参数名   传入键值对         1.直接传字典  2.正常调用
def PrintMsg2(**kwargs):
    print(kwargs)

#PrintMsg2(name='jerry',age=20)         #正常调用
info={'name':'jerry'}
#PrintMsg2(**info)                      #前面加**号 直接传字典 #{'name': 'jerry'}
#PrintMsg2(**{'name':'tom','age':'50'})  #{'name': 'tom', 'age': '50'}



#学习高阶函数
#1.1 将函数名作为参数变量使用
#1.2 函数名可以作为参数,也可以作为函数的返回值
def f(n):
    return n*n
print(f(6))

def foo(a,b,func):  #将函数作为参数传入
    ret= func(a)+func(b)
    return ret

print(foo(1,2,f))  #f作为参数 传入方法



#1.2 函数名可以作为参数,也可以作为函数的返回值
def test2():
    def inner():
        return  8
    return  inner()

test2()











