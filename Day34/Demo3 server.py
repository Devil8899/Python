#_author: liuz
#date: 2017/12/25
import socket,time
#IO非阻塞的例子  通过设置setblocking  可以一直循环获取发送或接收数据
sk=socket.socket()
sk.bind(('127.0.0.1',8016))
sk.listen(3)
#循环调用是否发送了数据
sk.setblocking(False)  #设为非阻塞模式 。非阻塞模式下，如果调用recv()没有发现任何数据，或send()调用无法立即发送数据，那么将引起socket.error异常。
while True:
    try:
        conn, address = sk.accept()  # 阻塞状态
        print(address)
        data = conn.recv(1024)
        print(data.decode('utf8'))
        conn.sendall(data)
        conn.close()
    except Exception as e:
        print('error',e)
        time.sleep(3)