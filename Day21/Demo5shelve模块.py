#_author: liuz
#date: 2017/12/14

import shelve
#可以实现文件读取和数据的序列化
#shelve模块比pickle模块简单 只有一个open()函数，返回一个类似字典的对象
#可读可写的key必须为字符串，而值可以是python所支持的数据类型

#写入open()
f=shelve.open('testntxt')
#f['info']={'name':'liuz'}
#读取get()
data=f.get('info')
print(data)


