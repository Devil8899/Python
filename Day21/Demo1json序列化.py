#_author: liuz
#date: 2017/12/14

#序列化  json  #我们把变量从内存中变成可存储或传输的过程称之为序列化，
#json是一个模块  但只能序列化 字典 列表  不能序列化函数 类


#没学json前  处理从文件读取的字典数据
#with open('test','r') as file:
#    data=file.read()
#    dd=eval(data)   #读取字符串  转换为字典通过 eval()函数
#    print(dd['age'])

import  json
dic={'age':20,'worker':'dirver'}

#dumps()方法返回一个str，内容就是标准的JSON
#要把JSON反序列化为Python对象，用loads()或者对应的load()方法
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化

#序列化
with open('test','a') as file1:
    str=json.dumps(dic)         #将字典转为字符串
    file1.write(str+'\r\n')     #将字符串写入文本

