#_author: liuz
#date: 2017/12/8

def test1(n):
    return n*n

def test2(a,b,test):               #把函数作为参数传递
    return test(a)+test(b)

#print(test2(1,2,test1))


#阶乘函数
'''
5！=5*4*3*2*1=120
7!=7*6*5*4*3*2*1=5040
'''
#用函数实现
#ftest1(5)=120
#fat(5)=120

def ftest1(n):
    ret=1
    while n>0:
        num = n - 1
        if num ==0:
            break
        if ret >1 :
            ret=ret*num
        else:
            ret=n*num
        n-=1
    return ret
print(ftest1(5))
#1*2*3*4*5的阶乘
def fat(n):
    ret=1
    for i in range(1,n+1):
        ret=ret*i
    return ret
print(fat(5))


print("______________________________________递归______________________________________________")
#递归recursion 完成阶乘
  # 1.函数内调用自己的函数
 # 2.有一个结束条件
#凡是递归可以解决的问题 循环都能解决
#在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
def fact2(n):
    #n=n*n-1
    if n==1:
        return 1
    return  n*fact2(n-1)
print(fact2(5))


'''
递归函数的优点:是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
递归特性:
1. 必须有一个明确的结束条件
2. 每次进入更深一层递归时，问题规模相比上次递归都应有所减少
3. 递归效率不高，递归层次过多会导致栈溢出
(在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，
栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。)
'''

#实例2(斐波那契数列) F[n]=F[n-1]+F[n-2](n>=2,F[0]=0,F[1]=1)
#0、1、1、2、3、5、8、13、21、34


def FeiboNa(n):
    if n==0 or n==1:
        return n
    return  FeiboNa(n-1)+FeiboNa(n-2)

print(FeiboNa(5)) #是5


















def fibo(n):

    before=0
    after=1
    for i in range(n-1):
        ret=before+after
        before=after
        after=ret

    return ret

print(fibo(3))
