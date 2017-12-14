#_author: liuz
#date: 2017/12/14
import  json
#读取字符串 转换为本来的数据类型loads()
with open('test','r') as file:
    data=file.read()  #返回一个字符串
    dic=json.loads(data)  #loads() 从字符串中转换为对象原来的类型-字典
    print(dic['worker'])

#json 不能序列化 函数 类

with open('test2','w') as file2:
    file2.write('[1,2,3,4,5]')

with open('test2','r') as file3:
    data2=file3.read()
    list2=json.loads(data2)
    print(list2[0])

