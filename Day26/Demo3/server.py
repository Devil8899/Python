#_author: liuz
#date: 2017/12/18

import socket

so=socket.socket()
so.bind(('127.0.0.1',8800))
so.listen(3)
print("wait...")


while True:
    conn, add = so.accept()  # 等待客户端连接 返回一个元祖
    while True:
         sendval=input("jack发送:")
         if sendval=="exit":
             conn.close()
             break
         conn.send(bytes(sendval,'utf8'))  #发送数据必须是字节类型
         revcdata=conn.recv(1024)          #接收数据指定大小
         print("eason发来了消息:",str(revcdata,'utf8'))
so.close()