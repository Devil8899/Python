#_author: liuz
#date: 2017/12/8

#学习函数

#1.定义函数 def

def logger(loggertxt):
    f=open('log.txt','a')
    f.write('2017 %s'%loggertxt+'\n')
    f.close()
    print('2017 %s'%loggertxt)


print("______________1")
logger("tom")
print("______________2")
logger("tom2")
print("______________3")
logger("tom3")