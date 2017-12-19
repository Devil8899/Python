#_author: liuz
#date: 2017/12/18

class People:
    __v=None
    @classmethod
    def people_getinstance(cls):
        if cls.__v :
            return cls.__v
        else:
            cls.__v=People()
            return cls.__v

#使用单例模式后 就不用下面方式创建实例了
# p1=People()
p2=People.people_getinstance()
p3=People.people_getinstance()
print(p3,p2)