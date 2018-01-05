#_author: liuz
#date: 2018/1/4

import socket
'''
所有web框架都是通过socket进行扩展的
这里已经实现了给浏览器发送一个信息 一个简单的web框架
这个接口就是WSGI：Web Server Gateway Interface。省略了我们写底层代码,这也是python默认的web服务器主要是测试用
'''
def handle_request(client):

    buf = client.recv(1024)  #http请求信息
    print(buf.decode('utf8'))
    client.send("HTTP/1.1 200 OK\r\n\r\n".encode("utf8"))
    with open('index.html','rb')as f:
        # client.send("<h1 style='color:red'>Hello,master</h1>".encode("utf8"))
        data=f.read()
    client.send(data)
def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost',8001))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()

if __name__ == '__main__':

    main()