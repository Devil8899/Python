#_author: liuz
#date: 2017/12/25
import select
'''
select 可以监控多个socket对象
select主要用于socket通信当中，能监视我们需要的文件描述变化。
上面的代码是通过IO不阻塞来执行socket 只能是一个socket对象
这里的例子是通过select模块里面的select方法来监控多个socket对象
'''
import socket
sk1=socket.socket()
sk1.bind(('127.0.0.1',8016))
sk1.listen(3)

sk2=socket.socket()
sk2.bind(('127.0.0.1',8017))
sk2.listen(3)
# print('test')
#绑定多个socket
while True:
    r, w, e = select.select([sk1, sk2], [], []) #代表了监控socket对象的文件描述符 #3个返回值
    # print('test2')
    for obj in r:
        conn, addr = obj.accept()  #r代表了被监控的socket对象
        conn.send('sayhi'.encode('utf8'))
        print(addr)
        print(conn.recv(1024).decode('utf8'))
    print(r)
#[<socket.socket fd=356, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8017)>]