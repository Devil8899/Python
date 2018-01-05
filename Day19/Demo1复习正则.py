#_author: liuz
#date: 2017/12/14
import  re
#匹配0个或1个2个连着字母 /或 匹配2个连着数字
ret=re.search('(?P<name>\w{2})/(?P<age>\d{2})','45bd/34h"ab')
# print(ret.group())
# print(ret.group('name'))
# print(ret.group('age'))
#P<name>   代表组
#在findall 里面()  代表组  只返回匹配组的信息
ret2=re.findall('www.(\w+).com','www.sina.com')
#print(ret2)   #['sina']

#finditer 返回一个迭代器对象 通过for循环 或者 next取值
retn=re.finditer('\d','sjd1,23,23')
#print(next(retn).group())
#for i in retn:
#     print(i.group())
