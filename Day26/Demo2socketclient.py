#_author: liuz
#date: 2017/12/18

#1.创建一个socket客户端
import socket
sockclient=socket.socket()
#2.创建连接  (服务器address,端口)
address=('127.0.0.1',8000)
sockclient.connect(address)
#发送数据
sockclient.send(bytes('测试','utf8'))
#接收数据
#data=sockclient.recv(1024)         #阻塞
#print(str(data,'utf8'))