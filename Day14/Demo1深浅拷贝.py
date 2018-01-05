#_author: liuz
#date: 2017/12/7
import  copy
#学习深浅拷贝

#列表  copy()方法  浅拷贝
'''
浅拷贝
    如果拷贝的列表中存在子列表
    那么拷贝的变量和新的指向的子列表的内存都是一个
    但是列表中的其他元素 另开辟了一个内存
    所以子列表修改  变量都会受影响，其他元素不会受影响

浅拷贝copy()                  只拷贝第一层     子列表修改互相影响
深拷贝(调用模块copy)           克隆一份         互相修改无影响
    
    copy对象：2个方法
        copy(拷贝对象)
        deepcopy(拷贝对象)  

'''

#修改无影响
s=[1,'tom','2017-10']
s2=s.copy()    #调用列表方法 实现浅拷贝
s2[0]=2
#print(s)
#print(s2)

#修改影响赋值前变量
s3=[[1,2],'jerry','2017']
# s4=s3    #内存地址都指向了一个   一改都会改变
#s4=s3.copy()
#s4[0][0]=10

#print(s4)
#print(s3)
#s3 修改列表有影响   修改字符串没有影响

#深拷贝

husband=['eason',10000,[100,200]]
wife=husband.copy()
wife[1]=20000
wife[2][1]-=10

#wife2=copy.copy(husband) #浅拷贝
wife2=copy.deepcopy(husband)#深拷贝deepcopy(拷贝对象)
wife2[0]='jack'
wife2[1]=30000
wife2[2][1]-=20 #克隆了一份对象

print(husband)
print(wife)
print("_____________________________深拷贝_________________________")
print(wife2)