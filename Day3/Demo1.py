#python3  默认支持中文 
#如果python2使用中文 会报错 除非在编译器第一行告诉编译器使用那个
#码表  语法：#!-*- coding:utf-8 -*-
#但是打印仍然是乱码  因为计算机默认是使用gb18030  在gb18030这个码表中与utf是不同的

'''两种写法 在python2版本中 改变码表的方式  还要加u'''
#!-*- codeing:utf-8 _*_
#codeing:utf-8
msg=u"你好 上海"     #加u 就是将本行代码改成了unicode编码 unicode 支持中文
print (msg)
#print type(msg)     #type 查看类型