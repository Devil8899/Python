#_author: liuz
#date: 2017/12/16
import  os
#多继承 ？ C++ and python
'''
python中可以同时继承多个父类
    1.如果父类存在同名方法时 优先级是从左到右 左边最高
    2.如果左边父类不存在此方法 如果父类也存在继承  会继续寻找上层父类
    3.如果继承的多个父类都是一个基类时 跟最后执行
'''
class fa:
    def run(self):
        print("fat  run")
class father1(fa):
    def run1(self):
        print("father1 is run")

class father2:
    def run(self):
        print("father2 is run")

class son(father1,father2):  #同时继承多个父类
      name='jerry'

s1=son()
#s1.run()  #fat  run




'''
Python pass是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句。
'''
'''
关于self的一个练习
当self在父类方法中调用一个方法时,如果这个方法在子类也存在 
会先调用子类的方法

'''
class people:
    pass

class Driver:
    def sing(self):
        print('doctor sing')
        self.Drive()  #这里self 代表的是stu  stu调用Drive 会先从自己的方法里调用 如果没有会找父类的方法
    def Drive(self):
        print("dirver a car")
class professor:
    def sing(self):
        print("professor sing")

class student(Driver,professor):
      def Drive(self):
          print("student Drive a car")

stu=student()
stu.sing()
'''
doctor sing
student Drive a car
'''