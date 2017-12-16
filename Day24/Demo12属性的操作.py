#_author: liuz
#date: 2017/12/16
import os
'''
属性就是成员字段
getattr(obj, name[, default]) : 访问对象的属性。
hasattr(obj,name) : 检查是否存在一个属性。
setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
delattr(obj, name) : 删除属性。
'''


class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
emp1.age=10
print(hasattr(emp1, 'age'))    # 如果存在 'age' 属性返回 True。
print(getattr(emp1, 'age'))   # 返回 'age' 属性的值
print(setattr(emp1, 'age2', 8)) # 添加属性 'age' 值为 8
#print(delattr(emp1, 'age'))    # 删除属性 'age'
print(emp1.age2)