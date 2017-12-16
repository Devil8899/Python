#_author: liuz
#date: 2017/12/16
import  os
#函数式编程
    #def + 函数名(参数)

#面向对象编程
#定义  关键字class
'''
class 类名
    foo() 定义方法名
    
class bar
    driver():
        print('行驶中')
Bar=bar()
Bar.driver()

调用执行：
    函数：
        函数名(参数)
    面向对象:
        中间人(对象/实例)=类名()  创建一个中间人访问foo()方法 创建对象
        实例.foo()   执行      
'''
#self 关键字  代指调用方法的对象 也就是中间人
class doctor:
    def work(self,wo):
        print(self,wo)
    def print2(self):
        print(self.name,self.gender)

dt=doctor()
print(dt)
dt.work('123')
'''self和dt 指向同一个内存空间
<__main__.doctor object at 0x000002900FCD7080>
<__main__.doctor object at 0x000002900FCD7080> 123
'''
#怎么使用self 因为self指向了当前创建的对象 所以self可以创建变量 并且将自己传到方法里面执行
dt.name='tom'
dt.gender='man'
dt.print2()
#这招可以在类外边进行封装字段 在类的方法里面调用 类似this
print(dt.gender)
