#_author: liuz
#date: 2017/12/16

#super方法键字 方法重写时调用父类方法用  super(子类名,self).父类方法名()
#父类.方法名()
#self代表当前调用的对象
class father:
    def eat(self):
        print("this is father eat fun")

class son(father):
    def eat(self):
        #super(son,self).eat()  #1.执行父类方法   super(son,self).父类方法名
        father.eat(self)        #2.执行父类方法   父类名.方法名()
       # print("this is son eat fun")
'''
当子父类方法同名时,默认会调用子类的同名方法，如果想调用父类的同名方法需要使用
super()方法
或者在子类方法里面使用
父类.方法名()的方式进行调用
'''
Son1=son()
Son1.eat()
'''
this is father eat fun
this is son eat fun
'''