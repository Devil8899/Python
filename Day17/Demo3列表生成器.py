#_author: liuz
#date: 2017/12/10
'''
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，
如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，
那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，
从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

'''


#生成器2种创建方式          生成器都是迭代器
#1. w=(x*2 for x in range(1,5))
#2. yield关键字生成


#列表生成式
#w=[x*2 for x in range(10)]

#1.创建一个生成器对象  并没有返回数据  生成器是一个可迭代对象
w=(x*2 for x in range(1,5))
#print(w)  #<generator object <genexpr> at 0x000001F829696938>


#生成器对象 1.内部方法__next__()  一般不使用  in python2 w.next()
#print(w.__next__())  #2 返回第一个元素


#2.next()方法=w.__next__()  建议使用系统内置方法
#print(next(w))     #2 返回第一个元素

#循环取所有值  生成器是一个可迭代对象(Iterable) for循环也是调用了内部的next方法
'''
for i in w:
    print(i)
'''

#2.Create_foo() 不再是一个方法 而是一个生成器对象
# 返回的是一个对象 而不是执行里面的语句
def Create_foo():
    print("msg")
    yield   1   #关键字yield 可以想成return语句 中断循环
    print('msg2')
    yield   2
    #return  None
#print(Create_foo())  #<generator object Create_foo at 0x0000029A8B4C6A40>
g1=Create_foo()
#next(g1)
#next(g1)
'''
msg
msg2
'''

#for i in Create_foo():
#    print(i)

'''
msg
1
msg2
2
'''


#什么是可迭代对象  对象拥有iter()方法才是
list_test=[1,2,3]
list_test.__iter__()

tuple_test=(1,2,3)
tuple_test.__iter__()

D_test={"name":'jerry'}
D_test.__iter__()


#打印斐波那契
#0 1 1 2 3 5 8 13 21
def  fmy(max):
    n,after,before=0,0,1
    while n<max:
        #print(after)
        yield after                           #生成器对象
        #after,before=before,after+before
        tmp=before
        before=after
        after=tmp+after
        n=n+1

after2=fmy(8)
print(next(after2))
print(next(after2))



#send()  方法 可以同时给变量赋值 并且next()


def printMsg():
    print("msg1")
    count=yield 1               #count=eeeeeeeee
    print(count)
    print("msg2")
    yield 2

b=printMsg()
#next(printMsg())
b.send(None)#next(b)             #第一次send前如果没有next(),只能传一个send(None)
b.send('eeeeeeeee')




'''
重点就是generator和函数的执行流程不一样。函数是顺序执行，
遇到return语句或者最后一行函数语句就返回。而变成generator的函数，
在每次调用next()的时候执行，遇到yield语句返回，
再次执行时从上次返回的yield语句处继续执行。
'''







'''
emp={
    'name':'tom',
    'job':'driver'
}
for key in emp:
    print(key,emp[key])
'''