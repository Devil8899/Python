#_author: liuz
#date: 2017/12/20

import queue,threading
#queue #线程队列
#　适用于多线程编程的先进先出数据结构，可以用来安全的传递多线程信息。
#  线程之间数据共享
#1.创建对象
d=queue.Queue()
#2..插入数据
d.put('jerry')
d.put('tom')
d.put('jack')
#先进先出FIFO
#print(d.get())  #jerry

'''
1. q = queue.Queue(maxsize=0)   
构造一个先进显出队列，maxsize指定队列长度，参数不填默认表示队列长度无限制。
2. q.join() 　　 
等到队列为kong的时候，在执行别的操作
3. q.put(item, block=True, timeout=None)   
   将item放入队列,如果block设置为True[默认]时,调用者将被阻塞,否则
   抛出Full异常,timeout设置阻塞超时
4. q.get(block=True, timeout=None) 
   从队列中取出一个项目
5. q.qsize() 返回队列大小
6. q.empty() 如果队列为空返回True,否则返回False
7. q.full()  如果队列满了返回True,否则返回False
'''

que = queue.Queue(10)
'''
Queue         先进先出
LifoQueue     先进后出
PriorityQueue 优先级队列模式
'''

def s(i):
    que.put(i)


def x(i):
    g = que.get(i)
    print('get', g)


for i in range(1, 11):
    t = threading.Thread(target=s, args=(i,))
    t.start()
print('size', que.qsize())
for i in range(1, 11):
    t = threading.Thread(target=x, args=(i,))
    t.start()

print('size', que.qsize())