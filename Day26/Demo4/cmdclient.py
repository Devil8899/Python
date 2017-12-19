#_author: liuz
#date: 2017/12/19



import socket
'''
循环读取接收的数据
'''
sk=socket.socket()
sk.connect(('127.0.0.1',8019))   #请求连接
print("客户端已启动...")
while True:
    val=input("发送内容:>>")
    if val=='exit':
        break
    sk.send(bytes(val,'utf8'))
    result_length=int(str(sk.recv(1024),'utf8'))
    # print(str(result_length))  #第一次获取返回的字节长度
    sk.send(bytes('已经收到了长度','utf8'))
    data=bytes()
    while len(data)!=result_length:  #循环读取返回的字节
          recv=sk.recv(1024)
          data+=recv
    print(str(data,'gbk'))  #因为数据是gbk编码 所以要按照gbk进行解码
sk.close()