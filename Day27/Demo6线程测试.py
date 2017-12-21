#_author: liuz
#date: 2017/12/20

import time,threading

def movie(name):
    print("movie start")
    time.sleep(4)
    print('movie player',name)
def music(name):
    print("music start")
    time.sleep(5)
    print("music player",name)
threads=[]
t1=threading.Thread(target=movie,args=('1932',))
threads.append(t1)
t2=threading.Thread(target=music,args=('彩虹',))
threads.append(t2)
if __name__=="__main__":
    for i in threads:
        i.setDaemon(True)  #设置为后台线程
        i.start()


print("___main____end")

'''
开启了3个线程执行
主线程和2个子线程同时执行(并行),但实际上3个线程在进入解释器GIL是在同一时间只有一个线程在工作，
他底层会自动进行上下文切换.这个线程执行点，那个线程执行点！
所以看不出来,但如果是计算密集型,效率不会比串行(一个一个)执行要快
'''