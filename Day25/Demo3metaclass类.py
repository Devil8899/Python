#_author: liuz
#date: 2017/12/18
import os


#python的基类是object 所有的类都继承与object

#学习 metaclass type()
#可以学习廖雪峰的python教程
'''
obj 是test类的一个对象
同样 type()是一个类
test2就是type的一个对象
总结：
    类都是type类的对象
    平时称谓的对象是类的一个实例
'''
#定义一个创建类  派生与type类
class myTypeclass(type):
     def __init__(self,*args,**kwargs):
         print("是type类的子类")
     def __call__(self, *args, **kwargs):  #这里self是一个test类  因为 test是myTypeclass的一个对象
         print("执行call方法")

class test(object,metaclass=myTypeclass):
    #object只是被省略了  metacalss=指定创建类
    #要控制类的创建行为，还可以使用metaclass。
    # #实际也是调用type()创建的类 会调用 type类的构造方法等等
    #test类就是myTypeclass的一个对象 可以理解  test=myTypeclass() 所以会执行__init__
        def print2(self):
            print("msg")

        # def __new__(cls, *args, **kwargs):


obj=test()

#另一种声明类的方式
test2=type('test2',(object,),{'func':lambda x:20})  #声明一个类test2,类中有一个成员func方法



'''
复习下lamdba
关键字lambda表示匿名函数 冒号前面的x表示函数参数。
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x * x
f()
同样，也可以把匿名函数作为返回值返回，比如：
def build(x, y):
    return lambda: x * x + y * y
f = lambda x: x * x
print(f(2))  #4
'''
'''
type 的使用
type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
要创建一个class对象，type()函数依次传入3个参数：
    1.class的名称；
    2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，
仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
正常情况下，我们都用class Xxx...来定义类，但是，
type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，
这和静态语言有非常大的不同，要在静态语言运行期创建类，
必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，
本质上都是动态编译，会非常复杂。
'''
'''
def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)
 Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
 h = Hello()
 h.hello()
    Hello, world.
 print(type(Hello))
    <type 'type'>
 print(type(h))
    <class '__main__.Hello'>
'''

#通过myTaclass创建类的过程
class sonclass(type):
    def __int__(self):             #self=docter
        print("this is 创建类")
    #def __new__(cls, *args, **kwargs):
     #   print("sonclass 被调用了")
    def __call__(self, *args, **kwargs):
       obj=self.__new__(self,'',(),dict)
       self.__init__(obj)

class docter(metaclass=sonclass):  #创建类 指定为sonclass
      print("docter")
      def __new__(cls, *args, **kwargs):
            return "对象"   #newobj是在这里被创建的
newobj=docter()

#分2阶段执行  1.解释器从上而下执行代码创建docter类
#2.通过docter类创建newobj对象