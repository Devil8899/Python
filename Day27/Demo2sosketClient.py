#_author: liuz
#date: 2017/12/19

#客户端
import socket


ip_port = ('127.0.0.1',8009)
sk = socket.socket()
sk.connect(ip_port)
sk.settimeout(5)
print("wait connect...")
while True:
    data = sk.recv(1024)
    print('receive:',str(data,'utf8'))
    inp = input('please input:')
    sk.sendall(bytes(inp,'utf8'))
    if inp == 'exit':
        break

sk.close()