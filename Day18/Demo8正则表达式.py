#_author: liuz
#date: 2017/12/12

#学习正则表达式

s='hello world'
# print(s.find('1'))
# ret=s.replace('ll','xx')
# print(ret)
# print(s.split(' '))  #['hello','world']

#正则表达式  模糊匹配

import  re

#1.字符匹配   大多数字母和字符通过自身匹配
#1.findall(pattern,string,flags)  全部找到  结果返回到列表中
'''
pattern	匹配的正则表达式
string	要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
'''
ret=re.findall('w\w{2}l','hello world')  #全部匹配worl  结果返回到列表中
#print(ret)   #['worl']
ret2=re.findall('tmo','tmo1tmo2')
#print(ret2)#['tmo', 'tmo']

#2.元字符： . ^ $ * + ?  {}  [] | () \

# . 代表任意一个字符  除换行符          .通配符
ret3=re.findall('w..l','hello world')       #匹配w开始任意两个字符l结尾的字符  【‘worl’】
# ^ 从字符串开始进行匹配
ret4=re.findall('^h...o','hellojsakdfho')  #['hello']
# $ 从字符串结尾进行匹配   被匹配字符必须位于结尾处
ret5=re.findall('t..m$','jsjdfmsdtoom')    #['toom']
# * 重复匹配      匹配0或多个的表达式。
ret6=re.findall('a.*t','falertdaler')      #['alert']
#print(re.findall('b*','bb'))        #匹配0个或多个b #['bb', '']
# + 重复匹配      匹配1个或多个的表达式。  匹配b前面有1个或多个a
ret7=re.findall('a+b','aabcbab')   #['aab', 'ab']
# ? 匹配0个或1个由前面的正则表达式定义的片段  匹配b前面有0个或1个a
ret8=re.findall('a?b','bsjaaba1b')  #['b', 'ab', 'b']

#{}   多次重复              b前面a重复5次
ret9=re.findall('a{5}b','aaaaaab')  #['aaaaab']
                    #匹配b前面1-3次a   属于贪婪匹配
ret10=re.findall('a{1,3}b','aaaaaab') #['aaab']

'''
*等于{0,正无穷}
+等于{1，正无穷}
?等于{0,1}
'''
#[] 字符集  取消元字符的特殊功能(\ ^ - 没有被取消)

ret11=re.findall('a[x,d]b','axb') #['axb']  1.或者的关系 x 或d
ret12=re.findall('[a-z]','adx')  #2.表示范围 a-z #adx
ret13=re.findall('[w,*]','*sdfw')  #3.取消元字符的特殊功能 ['*', 'w']
#^放到括号内 取反   -  ^  \
ret14=re.findall('[1-9a-zA-Z]','12pyY') #['1', '2', 'p', 'y', 'Y']
ret15=re.findall('^iu','iuzz')  #['iu']   从字符串开始进行匹配
ret16=re.findall('[^i,u]','iuzz')#[z,z]  取反的意思


#\
#反斜杠后边跟元字符去特殊功能
#反斜杠后边跟着普通字符实现特殊功能
'''
\d	匹配一个数字字符。等价于 [0-9]。
\D	匹配一个非数字字符。等价于 [^0-9]。
\s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
\S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
\w	匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
\W	匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。
\b  匹配一个单词边界(特殊字符)，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
'''
ret17=re.findall('\d{11}','sjdf1234567891011')  #['12345678910']
ret18=re.findall('\sasd','sjdk asd')  #[' asd']
re.findall('\Sasd','sjdkasd')
ret19=re.findall('\w','1Aj')  #['1', 'A', 'j']
ret20=re.findall(r'\bis','th#isd  is  my car') #['is', 'is']#捕捉单词边界

#() 小括号 分组   | 或者
#print(re.search('(as)+','ajsdjkasas').group())
print(re.search('(as)|d','as').group())




#########################################################

#re.search(pattern,string,flags) 扫描整个字符串并返回第一个成功的匹配。 返回一个对象  没找到 返回None
'''
pattern	匹配的正则表达式
string	要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。


'''
ret21=re.search('ld','ajdsldsddsd')
#通过对象方法group()获取返回的对象值
#print(ret21.group())  #ld
#print(re.search('a\.','a.sdj').group())  #a.

##  \\   用法
retN=re.findall(r'\\h','asjd\h')
print(retN)


#在 re中 \\-->\ 双\代替一个\
#在python解释器中
retn2=re.search(r'\bblow','blow').group()
print(retn2)