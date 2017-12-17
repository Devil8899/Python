#_author: liuz
#date: 2017/12/17

#属性的另一种写法
# 变量名=property(fget=方法名,fset=方法名,fdel=方法)
# 变量=property(方法名,方法名...)            更简单的写法
class people:
    def __init__(self,name):
        self.Name=name


    def getname(self):
        return self.Name

    def setname(self,v):
        self.Name=v
        print(v)
    # 定义属性 通过fget fset对应的方法 执行赋值和获取值操作等等
    name = property(fget=getname, fset=setname)# fdel=


chinese=people('liyang')

print(chinese.name)  #获取值操作
chinese.name='zhangsan' #修改值操作  自动执行 fset对应的方法setname
print(chinese.name)
