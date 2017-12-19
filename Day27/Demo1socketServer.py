#_author: liuz
#date: 2017/12/19
#多线程并发聊天
import socketserver  #引入模块
'''
server端实现并发聊天
SocketServer内部使用 IO多路复用 以及 “多线程” 和 “多进程” ，
从而实现并发处理多个客户端请求的Socket服务端。
即：每个客户端请求连接到服务器时，Socket服务端都会在服务器是创建一个“线程”或者“进 程” 
专门负责处理当前客户端的所有请求
'''
#ThreadingTCPServer实现的Soket服务器内部会为每个client创建一个 “线程”，该线程用来和客户端进行交互。
'''
使用ThreadingTCPServer:
1.创建一个继承自 SocketServer.BaseRequestHandler 的类
2.类中必须定义一个名称为 handle 的方法
3.启动ThreadingTCPServer
'''
class MyServer(socketserver.BaseRequestHandler):
    def handle(self): #定义handle方法
        # print self.request,self.client_address,self.server
        conn = self.request #如果连接请求过来，获取client端对象
        conn.sendall(bytes('欢迎:请输入1xxx,0转人工服务.','utf8')) #发送一个信息
        Flag = True #并把Flag设置为True
        while Flag: #当Flag为True的时候执行
            data = str(conn.recv(1024),'utf8') #接收client端数据
            print(self.client_address)
            if data == 'exit': #判断如果data  == 'exit' 退出
                Flag = False #并把Flag设置为Flase
            elif data == '0': #如果为 == ‘0’
                conn.sendall(bytes('通过可能会被录音','utf8')) #发送数据
            else:#上面的都没匹配上，发送请重新输入
                # conn.sendall(bytes('请重新输入.','utf8'))
                 conn.sendall(bytes(input(">>"),'utf8'))


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8009),MyServer)
    #实例化对象，设置启动的IP/PORT并把自己定义的类写上作为SocketServer.ThreadingTCPServer的构造函数
    server.serve_forever() #调用对象中的启动方法

'''
ThreadingTCPServer 继承与：ThreadingMixIn, TCPServer
TCPServer有__init__方法

'''