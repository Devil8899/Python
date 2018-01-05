#_author: liuz
#date: 2017/12/14

import shelve
#可以实现文件读取和数据的序列化
#shelve模块比pickle模块简单 只有一个open()函数，返回一个类似字典的对象
#可读可写的key必须为字符串，而值可以是python所支持的数据类型
#shelve类似于一个存储持久化对象的持久化字典，即字典文件
#写入open()
f=shelve.open('testntxt')  #打开一个文件
#f['info']={'name':'liuz'}  #向文件中添加内容，添加方式与给字典添加键值对相同
#读取get()
# data=f.get('info')
# print(data)
print(f['info'])
# f.close()  #关闭文件

