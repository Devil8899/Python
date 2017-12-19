#_author: liuz
#date: 2017/12/18
import os
'''
Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，
而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。
server端
client端
'''
import socket

#1.创建socket对象 3个参数  都有默认值所以传入
so=socket.socket()
'''
参数一：地址簇
　　socket.AF_INET IPv4（默认）
　　socket.AF_INET6 IPv6
　　socket.AF_UNIX 只能够用于单一的Unix系统进程间通信
参数二：类型
　　socket.SOCK_STREAM　　流式socket , for TCP （默认）
　　socket.SOCK_DGRAM　　 数据报式socket , for UDP
　　socket.SOCK_RAW 原始套接字，普通的套接字无法处理ICMP、IGMP等网络报文，而SOCK_RAW可以；其次，SOCK_RAW也可以处理特殊的IPv4报文；此外，利用原始套接字，可以通过IP_HDRINCL套接字选项由用户构造IP头。
　　socket.SOCK_RDM 是一种可靠的UDP形式，即保证交付数据报但不保证顺序。SOCK_RAM用来提供对原始协议的低级访问，在需要执行某些特殊操作时使用，如发送ICMP报文。SOCK_RAM通常仅限于高级用户或管理员运行的程序使用。
　　socket.SOCK_SEQPACKET 可靠的连续数据包服务
参数三：协议
　　0　　（默认）与特定的地址家族相关的协议,如果是 0 ，则系统就会根据地址格式和套接类别,自动选择一个合适的协议
'''
#2.为socket绑定ip和端口号
address=('127.0.0.1',8000)
so.bind(address)
so.listen(3)  #客户端最大可以等待的人数
print("wait...")
conn,add=so.accept() #等待客户端连接 返回一个元祖
#3.使用conn对象

#接收
val2=conn.recv(1024)
print(str(val2,'utf8'))
#发送
#val=input(">>>")
#conn.send(bytes(val,'utf8'))
'''
socket各种方法：
    服务端方法:
so.bind(参数address)   参数必须是元祖   将套接字绑定到地址。address地址的格式取决于地址族。在AF_INET下，以元组（host,port）的形式表示地址。
so.listen(参数backlog) 开始监听传入连接。backlog指定在拒绝连接之前，可以挂起的最大连接数量。
        backlog等于5，表示内核已经接到了连接请求，但服务器还没有调用accept进行处理的连接个数最大为5 
        这个值不能无限大,因为要在内核中维护连接队列
so.accept()　接受连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
           　接收TCP 客户的连接（阻塞式）等待连接的到来
recv(bufsize[,flag])     接收 接受套接字的数据。数据以字符串形式返回，bufsize指定最多可以接收的数量
send(bufsize[.flag])     发送 将byte数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。即：可能未将指定内容全部发送。
sendall(string[,flag])   将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。
                         成功返回None，失败则抛出异常。
                         内部通过递归调用send，将所有内容发送出去。
close()                  关闭套接字
客户端使用连接服务器使用
    客户端方法:
so.connect(address) 连接到address处的套接字。一般，address的格式为元组（hostname,port）,如果连接出错，返回socket.error错误。
recv
send
'''