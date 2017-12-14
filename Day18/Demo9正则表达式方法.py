#_author: liuz
#date: 2017/12/13

import  re
'''
正则表达式方法
1.findall():所有结果返回到一个列表
2.search(): 返回匹配到的第一个对象 对象可以调用group()返回结果
3.Match():  只在字符串开始匹配
re.match与re.search的区别
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，
则匹配失败，函数返回None；而re.search匹配整个字符串
，直到找到一个匹配。
4.split()
5.sub(表达式,替换字符串，被替换字符串)   用于替换字符串中的匹配项。
6.compile() 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。
该对象拥有一系列方法用于正则表达式匹配和替换。
7.re.finditer() 返回一个迭代器对象 有next()方法来取值
'''
#ret=re.match('ad','adsjdk')
#print(ret.group())

ret2=re.split('[j,d]','sjkdjs')  #['s', 'k', '', 's']
# print(ret2)

#将找到的匹配项提成成df
ret3=re.sub('a..x','d..f','acvx1')  #d..f1
#print(ret3)

ret5=re.compile('\.[com,cn]{1,3}')
print(ret5.findall('sdj.com'))