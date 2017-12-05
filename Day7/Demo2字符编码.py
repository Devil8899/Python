#!-*- coding:utf-8 -*-
#指定了文件编码  python2中默认使用ASSIC
#_author: liuz
#date: 2017/12/5
s='年后'
s_to_unicode=s.decode('utf-8')  #将utf-8解码成unicode  要先声明你现在的格式
s_to_gbk=s_to_unicode.encode('gbk')#表示将unicode编码的字符串转换成gbk编码
print(s_to_unicode)             #unicode支持中文
print(s_to_gbk)                 #gbk
print(s)                        #utf-8

#将GBK转为utf-8

U_unicode=s_to_gbk.decode('gbk')  #将gbk转为unicode
U_utf=U_unicode.encode('utf-8')   #将unicode转为utf-8
print(U_utf)
