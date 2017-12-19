#_author: liuz
#date: 2017/12/18

import socket

sk=socket.socket()
sk.connect(('127.0.0.1',8800))

while True:
    data=sk.recv(1024)
    print("jack发来了消息:",str(data,'utf8'))  #接收数据 转为字符串
    val=input("eason输入:")
    if val=='exit':
        break
    sk.send(bytes(val,'utf8'))              #发送数据 转为字节发送
sk.close()