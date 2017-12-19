#_author: liuz
#date: 2017/12/19

#远程执行命令

import socket
import  subprocess  #subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
'''
客户端发送一个命令
服务端执行后将结果返回给客户端
发送数据长度太大时 可以先发送一个长度
然后将数据发送给客户端
客户端接收数据后循环读取
'''
sk=socket.socket()
#print(sk)
address=('127.0.0.1',8019)
sk.bind(address)
sk.listen(3)
print("服务已启动...")
while True:
    conn,adr=sk.accept()  #等待连接
    print("wait...")
    while True:
        try:
            data=conn.recv(1024)
        except   Exception:
            break
        if not data:
            break
        print("接收的内容:",str(data,'utf8'))
        #获取一个subprocess对象  开启了一个进程来进行处理 接收的客户端命令
        obj=subprocess.Popen(str(data,'utf8'),shell=True,stdout=subprocess.PIPE)
        # stdout=subprocess.PIPE    将子进程执行的结果 返回到主进程里面 都封装到了obj里面
        cmresuld=obj.stdout.read()  #返回的是一个字节数据  gbk编码
        #print(type(cmresuld))
        length=bytes(str(len(cmresuld)),'utf8')  #计算长度
        # print(">>>>>>",length)
        conn.sendall(length)
        conn.recv(1024)             #解决粘包 中间隔开 防止连续两个发送包在一起  粘包
        conn.sendall(cmresuld)      #发送一个字节数据 gbk编码


