#_author: liuz
#date: 2017/12/10

#列表生成式  通过指定格式返回一个列表
a=[x for x in range(10)]
print(a)  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#可以对x进行表达式操作
a1=[x*2 for x in range(10)]
print(a1)  #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

def f(n):
    return n**3
#也可以调用函数
a2=[f(x) for x in range(10)]
print(a2,type(a2))

#另一种简单的赋值方式
t=('123',99)
c,d=t
print(c,d)


