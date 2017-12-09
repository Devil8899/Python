#_author: liuz
#date: 2017/12/8

#函数返回值

def add(*args):
    print(args)
    num=0
    for i in args:
        num+=i
    return num        #1.return  结束参数  2.返回值
#注意
#3.函数如果没有return 默认返回一个null
#4.return 多个对象 系统自动将返回的数据 封装为一个元祖返回

num2=add(10,10,10)
print(num2)

def test():
    return 1,2,3,[1,2]
print(test())