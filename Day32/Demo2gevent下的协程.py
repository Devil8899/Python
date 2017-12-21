#_author: liuz
#date: 2017/12/21

from  greenlet import  greenlet
'''
1.引入模块greenlet
实现单线程并发效果
2.创建greenlet对象
3.调用switch() 方法 实现不同任务的切换
'''
def test1():
    print("12")
    gr2.switch()
    print("56")
    gr2.switch()
def test2():
    print("34")
    gr1.switch()
    print("78")
gr1=greenlet(test1)   #创建greenlet对象  传入一个方法
#print(gr1)           #<greenlet.greenlet object at 0x0000021BECAB85A0>
gr2=greenlet(test2)

gr1.switch()        #通过switch()方法完成不同任务的切换
#switch 类似与yield下的next()方法