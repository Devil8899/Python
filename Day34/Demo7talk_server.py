#_author: liuz
#date: 2017/12/25

import socket
import select

sk=socket.socket()
sk.bind(('127.0.0.1',6501))
sk.listen(3)
inp=[sk,]
index=1
while True:
    #可以监控socket也可以监控conn
    inputs,outputs,errors=select.select(inp,[],[],5)
    for s in inputs:
        if s==sk:
            conn,addr = s.accept()
            inp.append(conn)
        else:
            data = conn.recv(1024)
            print(data.decode('utf8'))
            inputs=input("server>>>")
            conn.send(inputs.encode('utf8'))

'''
这里实现一个伪并发的非阻塞IO执行效果
    1.是通过select方法监控,socket通信当中监视我们需要的文件描述变化。
    当变化时我们就返回一个socket对象 因为客户端连接的conn不同所以实现了
    客户机并发效果
'''
#这就是一个事件驱动模型  通过队列处理 比如点击事件 加入了队列中，有个循环不断从高队列中取出事件，根据不同事件调用不同函数