#_author: liuz
#date: 2017/12/14
import  json
#dump()  序列化的同时写入文本
#load()  反序列化的同时读取文本

dic={'age':20,'worker':'dirver'}
f=open('testn','w')
#序列化的同时写入文本
json.dump(dic,f)
f.close()


f2=open('testn','r')
#读取数据的同时反序列为数据
data=json.load(f2)   #省略了读取的代码
print(data['worker'])

#pickle 里面的dump()  和  load() 方法  与上面相同

