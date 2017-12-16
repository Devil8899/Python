#_author: liuz
#date: 2017/12/16


class people:
    name='tom'         #静态字段
    def __init__(self,age):
        self.age=age  #成员字段
        people.name+='1'


peo=people('20')
print(people.name)
print(peo.age)
print(peo.name)
'''
类成员:
        字段： 
             普通字段：保存在对象中，只能通过对象访问
             静态字段：保存在类中    执行可以通过对象访问  也可以通过类名.字段名 访问
        方法：
            
'''


