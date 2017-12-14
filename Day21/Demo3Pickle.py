#_author: liuz
#date: 2017/12/14

import pickle
#这个模块可以把任意对象序列化  但都是以字节数据进行存储的 读取的
#pickle.dumps()方法把任意对象序列化成一个bytes字节类型，
#然后,就可以把这个bytes写入文件。
#或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：


#当我们要把对象从磁盘读到内存时，
# 可以先把内容读到一个bytes，
# 然后用pickle.loads()方法反序列化出对象，
# 也可以直接用pickle.load()方法从一个file-like Object
# 中直接反序列化出对象。

#dumps()

def print2():
    print('def print3')

#序列化
f=open('testn','wb')      #以二进制的字节数据的方式写入文本中
data=pickle.dumps(print2) #dumps()方法把任意对象序列化成一个bytes字节类型
f.write(data)
f.close()


#反序列化
f2=open('testn','rb')
data2=pickle.loads(f2.read())  #读到的内容反序列化出对象
data2()