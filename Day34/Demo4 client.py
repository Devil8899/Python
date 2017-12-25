#_author: liuz
#date: 2017/12/25
import socket

sk=socket.socket()
sk.connect(('127.0.0.1',8016))
while True:
    # inp=input(">>")
    sk.sendall('hi'.encode('utf8'))
    data=sk.recv(1024)
    print(data.decode('utf8'))
