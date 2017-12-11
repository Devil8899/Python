#_author: liuz
#date: 2017/12/11



import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield
       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))
       #yield

def producer(name):
    c = consumer('jerry')              #生成器对象
    c2 = consumer('tony')             #生成器对象
    c.__next__()
    c2.__next__()
    print("开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)

producer("tom")