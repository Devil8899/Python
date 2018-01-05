#_author: liuz
#date: 2017/12/18
import os
#try except 异常处理

'''
Exception 所有异常类  信息都会被捕捉到
异常处理类
AttributeError 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
IOError 输入/输出异常；基本上是无法打开文件
ImportError 无法引入模块或包；基本上是路径问题或名称错误
IndentationError 语法错误（的子类） ；代码没有正确对齐
IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError 试图访问字典里不存在的键
KeyboardInterrupt Ctrl+C被按下
NameError 使用一个还未被赋予对象的变量
SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
TypeError 传入对象类型与要求的不符合
UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，
导致你以为正在访问它
ValueError 传入一个调用者不期望的值，即使值的类型是正确的

'''
try:
    pass
    #代码 逻辑
    i=int(input("输入数字>>"))
except Exception as e:
    #e是Exception对象 对象中封装了错误信息
    i=1   #代码出错后执行
print(i)

#需要考虑所有可能出现的异常，可以这么写
s1 = 'hello'
try:
    int(s1)
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:  #用这个万能的异常去捕获异常
    print(e)
else:
    print("没有错误")
finally:
    print("我一定会被执行")
#try else
#try fin


print("____________________主动抛出异常 raise 关键字___________________________")
class model:
    @classmethod
    def connect(cls):
        return False

try:
    result = model.connect()
    if result:
            print ("1m连接成功")
    else:
        raise Exception('\033[31;1m无法连接数据库\033[0m')#无法连接的时候主动触发一个异常，这个异常的明细，是我自己来指定的
except Exception as e:
             print(e)

'''
try:
    #这一块才是最主要的逻辑处理块，所有的逻辑处理都是放在这里的
    pass
except KeyError,e:#如果出现KeyError错误，首先被他捕获，下面的except就不执行了
    pass
except Exception,e:#如果上面的错误没有找到就去，万能异常里找
    pass
else:#这里什么时候执行呢，逻辑代码里为出现异常这个代码快才执行
    pass
finally: #不管上面是否出现异常,最后执行完之后，这里永远执行！finally什么时候用？你上面执行一个操作，连接数据库，我这里就可以执行，断开数据库释放资源！（举例）
    pass

'''

print("——————————————————————————————————————自定义异常类————————————————————————————————")

class myException(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg

try:
    raise myException("\033[31;1m主动抛出 自定义异常类捕获\033[0m")
except myException as e:
    print(e)

#assert  条件/断言 AssertionError 用于用户强制服从,不服从就报错  可以捕获 但是一般不捕获
#print("jsd")
#assert 1==2
#print("jsdk")