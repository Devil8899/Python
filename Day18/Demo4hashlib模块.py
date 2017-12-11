#_author: liuz
#date: 2017/12/11

#加密模块  从明文到密文

import hashlib

m1=hashlib.md5()  #获取Md5对象
print(m1)
m1.update('thisistest'.encode('utf-8')) #默认是unicode需要转换为utf-8
#print(m1.hexdigest()) #63d31762a50f937b535746c9e31fa33e

#对加密后的数据再次加密  相当于下面的方式
m1.update('jerry'.encode('utf-8'))
print(m1.hexdigest())  # 69e7f8fc2d5f928a2db75c872e53f57c

#其实是与上面的方式相同
m2=hashlib.md5()
m2.update('thisistestjerry'.encode('utf-8'))
print(m2.hexdigest())  # 69e7f8fc2d5f928a2db75c872e53f57c

#另一种算法sha256()
m3=hashlib.sha256()
m3.update('thisistestjerry'.encode('utf-8'))
print(m3.hexdigest())
