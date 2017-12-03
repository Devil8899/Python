# _author: liuz
# date: 2017/12/3

# 字符串string

# 1.定义
var = '123'
var2 = "2123'dsjk"
# print('hello'*20)   #多次打印

# 2.截取字符串  和切片一样  返回截取后的字符串
# print('thisString'[2:])

# 3.判断是否存在  关键字in
# print('el' in 'tel')
# rint(123 in [123,232])

# 4.格式化输出  占位符%s  %填充的字符串
# print('this is fu%s'%'nning')

# 5.拼接字符串  +  效率低 使用 join关键字 可以指定格式来拼接
a = '123'
b = 'abc'
# print(a+b)
#c = ''.join([a, b])
#print(c)
#print('------'.join([a, b]))


# _______________________________字符串内置方法————————————————————————————————————————————————

st='ni\thaon {name} age is {age}'

#print(st.count('n'))    #统计元素出现的个数
#print(st.capitalize())  #字符串首字母大写   Nihaon
#print(st.center(10,'-'))#--nihaon--  居中 剪掉字符串所占位置
# print(st.endswith('tty3')) #  判断是否以某个内容结尾   返回bool
# print(st.startswith('he')) #  判断是否以某个内容开头
#print(st.expandtabs(tabsize=10))#设置\t 大小

#print(st.find('p'))  #查找第一个元素并返回索引  不存在返回-1
#print(st.format(name='jerry',age='123'))#格式化字符串  先定义占位符{ },定义变量名=值
#print(st.format_map({'name':'jerry','age':'123'})) #格式化字符串 另一种定义写法
#print(st.index('j')) #返回索引 没有则报错
#print('123ba'.isalnum())#字母和数字   返回bool

'''
print('12378'.isdecimal())  # 方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。
print('123878'.isnumeric()) #方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。
print('1238781'.isdigit())  #isdigit() 方法检测字符串是否只由数字组成,不能包含小数点
'''
#print('abc'.islower())#判断是不是小写                  ********
#print('Abc'.isupper())#判断是不是全大写                ********
#print(' '.isspace())#判断是不是个空格
#print('Mytitle'.istitle()) #所有单词首字母大写


#print('Mytitle'.lower()) #大写变小写                   ********
#print('jsd'.upper())#小写变大写                        ********
#print('my Title'.swapcase())#反过来  大变小 小变大      ********

#print('sjd'.rjust(20,'*'))
#print('sj1d'.ljust(20,'*'))
'''
*****************sjd
sj1d****************
'''

#print('  djf'.strip())                         #去除空格  rstrip()去右边  lstrip()去左边
#print('mytitle'.replace('mytitle','newWord'))  #替换

print('mytitle'.rfind('t')) #返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1。
print('mylife life life'.split(' ')) #使用空格分隔 返回列表   ['mylife', 'life', 'life']
print('mylife life life'.split(' ',1)) #后面参数1代表分割一次  ['mylife', 'life life']

print('mylife life life'.split('i')) #['myl', 'fe l', 'fe l', 'fe']
'''
#将列表转为字符串
life='mylife life life'.split(' ')
print(','.join(life))   #mylife,life,life
'''

#title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())。