#_author: liuz
#date: 2017/12/16

#继承  好期待 C#  son:father  java  son extends father
    #子类继承父类  方法 等等

#语法 class 子类(父类名)

class father:           #父类 基类
    def eat(self):
        print("father eat def",self)
    def work(self):
        print("father is worker")
class son(father):    #继承  子类 派生类
    def work(self):
        print("son is worker",self)

Son=son()
Son.eat()  #子类继承父类的方法 调用父类eat方法        Self永远是指对象的调用者
Son.work() #子父类同名方法 会调用子类的 方法的重写