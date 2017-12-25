#_author: liuz
#date: 2017/12/25

import socket

so=socket.socket()
so.connect(('127.0.0.1',6501))
while True:
    inp=input("client>>")
    so.send(inp.encode('utf8'))
    data=so.recv(1024)
    print(data.decode('utf8'))