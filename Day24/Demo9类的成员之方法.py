#_author: liuz
#date: 2017/12/16

class car:
    def start(self):
        print("start car")
    @staticmethod
    def end():
        print("car end")

    @classmethod
    def pause(cls):
        print("car pause")
cr=car()
cr.start()
#cr.end()
car.end()
car.pause()
'''
1.成员方法  通过对象调用  self 当前对象
2.静态方法  通过类名调用 或者对象     @staticmethod 关键字
3.类方法    通过类名调用  cls  类名
'''
