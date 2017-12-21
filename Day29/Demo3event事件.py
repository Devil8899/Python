#_author: liuz
#date: 2017/12/20
import threading,time
'''event不是一个锁  用于主线程控制其他线程的执行
Python线程的事件，事件主要提供了三个方法:set、wait、clear
事件处理的机制：全局定义了一个‘flag’，如果‘flag’值为False，
那么当程序执行event.wait方法时就会阻塞，如果‘Flag’值为True，
那么event.wait方法时便不再阻塞
clear()  将‘Flag’设置为False
set()    将‘Flag’设置为True
isset() 返回event状态值

'''
def do(event,i):
    print('start',i)
    event.wait()               #线程被阻塞
    print('execute',i)

event_obj = threading.Event()    #1.创建一个event对象
for i in range(5):              #创建10个线程
    t = threading.Thread(target=do, args=(event_obj,i))
    t.start()

event_obj.clear()                #设置为false
# time.sleep(2)
inp = input('input:')
if inp == 't':
    event_obj.set()             #设置为true