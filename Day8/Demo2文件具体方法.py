#_author: liuz
#date: 2017/12/5

#处理文件的具体方法
'''
r  读
a 追加
w 写入
r+  读+写    追加到最后
w+  写加读   会先清空内容
a+  写追加   在文件末尾追加


read()       读取指定长度
readline()   读取一行
readlins()   读取整个文件  返回一个列表  效率不高

for i in f   将f作为整个文件读取 迭代器方式

tell()   取出光标位置
seek(参数)  调整光标位置  就是读取位置
flush() 清空缓存内容  写入到磁盘中
with()  创建文件 自动释放资源
'''


f=open('Usertxt','r',encoding='utf-8')
#读取1行   readline
#dataLine=f.readline()

#dataLine=f.read(5) #读取指定长度字符

#readlines() 返回一个列表 根据换行符 将所有行加入到列表中   ['牛渚西江夜，青天无片云。\n', '登舟望秋月，空忆谢将军。\n', '余亦能高咏，斯人不可闻。\n', '明朝挂帆席，枫叶落纷纷。']
#datalins=f.readlines()

'''
num=0
for i in datalins:  #循环列表  i代表了列表的一个对象
    num+=1
    if num==3:
        i=''.join([i.strip(),'iiiii']) #拼接在一起
    print(i.strip())
'''
#不用定义第三方变量 进行循环
'''
for index,linehh in enumerate (f.readlines()):
    if index==3:
        linehh=''.join([linehh.strip(),'newcontext'])
    print(index,linehh)
'''

#另一种读取文件方法  效率高 推荐使用
'''
number2=0
for i in f:   #这是一种迭代器方式 for内部将f对象做成一个迭代器，用一行取一行
    number2+=1
    if number2==2:   #处理文件
        i=''.join([i.strip(),'jiaru'])
    print(i.strip())
'''

#通过查看光标的变化 #一个英文占一个字符 一个中文占3个字符
#tell 取出光标位置
#seek 调整光标位置

#print(f.tell())
#print(f.read(2))
#print(f.tell())


#f.seek(0)  #丛头开始读取
#print(f.read(4)) #读取4个字符



#f.flush()

f.close()

#with 语句用来创建文件对象  with语句完成后 会自动释放资源
#同时创建多个对象 逗号隔开
'''
with  open('UserWrite','w') as f2,open('sdj','r')as f3:
    f2.readline()
    f2.read()
    print(f2)
'''