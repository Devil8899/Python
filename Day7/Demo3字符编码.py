#_author: liuz
#date: 2017/12/5

import  sys
print(sys.getdefaultencoding())  #打印文件默认编码

name='联想'

s_to_gbk=name.encode("gbk")  #unicode转成gbk
print(name)
print(s_to_gbk)  #会把数据转成byte类型 同时是gbk字节数据 b'\xc1\xaa\xcf\xeb'
print(s_to_gbk.decode("gbk")) #把gbk转为unicode

