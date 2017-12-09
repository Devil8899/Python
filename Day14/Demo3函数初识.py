#_author: liuz
#date: 2017/12/8

#学习函数

#1.定义函数 def
'''
 def 函数名(参数):
    函数体

'''

def logger(loggertxt):
    f=open('log.txt','a')
    f.write('2017 %s'%loggertxt+'\n')
    f.close()
    print('2017 %s'%loggertxt)


# print("______________1")
# logger("tom")
# print("______________2")
# logger("tom2")
# print("______________3")
# logger("tom3")


#写一个 日志方法   获取时间time模块
import  time
time_formt='%Y-%m-%d %X'  #定一个时间格式
time_full=time.strftime(time_formt) #获取当前系统时间
print(time_full)

def logerWrite(text):
    with open("log.txt",'a',encoding='utf-8')as fw:
        fw.write("当前时间:"+time_full+"\t"+'写入内容是'+text+'\n')


def action1(text):
    logerWrite(text)

def action2(text):
    logerWrite(text)


text=input("本次写入>>")

action1(text)
action2(text)
