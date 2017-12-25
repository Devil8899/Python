#_author: liuz
#date: 2017/12/25
import socket

sk=socket.socket()
sk.connect(('127.0.0.1',8016))
while True:
    data=sk.recv(1024)
    print(data.decode('utf8'))
    inp = input(">>")
    sk.send(inp.encode('utf8'))

