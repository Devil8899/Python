#_author: liuz
#date: 2017/12/16
import os
#在继承调用方法时一定要知道self是那个对象
'''
构造函数在继承的使用:
    1.如果子类存在构造函数 创建对象时会调用子类构造方法
    2.如果子类不存在构造函数 父类存在 那么会按照继承方法执行的顺序执行
    3.当构造方法执行结束后在执行对象调用方法
    
'''

class people:
    def __init__(self):
        print("people init")

class Driver(people):
    #def __init__(self):
    #    print("Driver init fun")
    def sing(self):
        print('doctor sing')
    def eat(self):
        print("driver eat fun")
class professor:
    def sing(self):
        print("professor sing")

class student(Driver,professor):
      #def __init__(self):
        #  print("student init fun")
      def Drive(self):
          print("student Drive a car")

stu=student()
'''
 1 class Person(object):
 2     def __init__(self,name,sex):
 3         self.name = name
 4         self.sex = sex
 5 
 6 class Child(Person):                          # Child 继承 Person
 7     def __init__(self,name,sex,mother,father):
 8         Person.__init__(self,name,sex)        # 子类对父类的构造方法的调用
 9         self.mother = mother
10         self.father = father
11 
12 May = Child("May","female","April","June")
13 print(May.name,May.sex,May.mother,May.father)    
'''
