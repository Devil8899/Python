# _author: liuz
# date: 2017/12/3
"""
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
和json对象格式差不多
d = {key1 : value1, key2 : value2 }
键必须是唯一的，但值则不必。  键和值是映射关系  列表和元祖是通过索引
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。

不可变类型： 整形,字符串,元祖
可变类型：列表，字典
"""

# 两个特点 键唯一,无序
dic = {'name': 'jerry', 'Age': 20, 'work': {'work1': 'professor'}, 'driver': True}

# 创建方式2 通过工厂函数
# a=list((1,2,3))              #工厂函数 创建列表
# b=dict((('Name','tom'),))    #{'name': 'tom'}  dict([['name','tom'],])  只要是个序列并且是键值对  python就认为是对的
# print(b)

# 增    无此键就是增  有此键是改
#dic['salary'] = 20000

# 增 setdefault()方法   如果键不存在于字典中，将会添加键并将值设为默认值 存在则不做操作
# 方法有返回值     键存在     返回字典相应键对应值
#                键不存在，在字典中中增加新的键值对，并返回相应的值
# 语法： 。 dict.setdefault(key, default=None)
#dic.setdefault('address', 'shanghai')


#查  通过键查找

'''
print(type(dic.keys()))   #获取所有键    数据类型<class 'dict_keys'>
print(list(dic.keys()))   #将所有键转为 列表
print(list(dic.values())) #所有值
print(list(dic.items()))  #items()键值对   将字典转为元祖 tuple  不允许修改
'''

#改
'''
dic['name']='eason'
dic2={'name':'jack','Mobile':1238237}
dic.update(dic2)    #扩展了dic字典,如果有相同键会覆盖                 {'name': 'jack', 'Age': 20, 'work': {'work1': 'professor'}, 'Mobile': 1238237, 'driver': True}
print(dic)
'''


#删
#del dic['name']  #单个键值对

#dic.clear()     #清空  但是是空字典

#dic.pop('键')  #返回删除的值
#print(dic.pop('Age'))

#	popitem()
#随机删除字典中的一对键和值。并以元祖返回值  类似：('driver', True)
#print(dic.popitem())

#del dic   #删除整个数组



#其他操作以及设计的方法

#创建 dict.fromkeys() 为多个键初始化值   但是修改一个  所有都会改变
'''
Newdic=dict.fromkeys(['name1','name2','name3'],['test','test2'])
print(Newdic)  #{'name3': ['test', 'test2'], 'name1': ['test', 'test2'], 'name2': ['test', 'test2']}
Newdic['name1'][1]='jerry'
print(Newdic)  #{'name2': ['test', 'jerry'], 'name3': ['test', 'jerry'], 'name1': ['test', 'jerry']}
'''


#字典嵌套
'''
data={
    'shanghai':{
        '1':['徐汇区','浦东新区'],
        '2':['静安区']
         },
    'Beijing':{
        '1':['迎宾大道'],
        '2':['长安街']
        }
      }
data['shanghai']['1'][1]='宝山区'
print(data)
'''

#排序  根据键排序   输入键是字符串 按照ASSIC码排序
dic2={1:'tom1',5:'tom2',2:'tom3'}
print(sorted(dic2))  #排序键  [1, 2, 5]
#print(dic2.items())  #一般将返回的items类型转换为列表使用  dict_items([(1, 'tom1'), (2, 'tom3'), (5, 'tom2')])
print(sorted(dic2.items())) # 排序键值对 dic2.items()   [(1, 'tom1'), (2, 'tom3'), (5, 'tom2')]


#遍历2种方式  i代表键
'''
for i in dic2:
    print(dic2[i])
'''

'''
for i,v in dic2.items():
    print(i,v)
'''