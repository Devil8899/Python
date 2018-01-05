#_author: liuz
#date: 2017/12/7

#学习Set集合                  无序,不重复
'''
集合是一个无序的，不重复的数据组合，它的主要作用如下：
去重，把一个列表变成集合，就自动去重了
关系测试，测试两组数据之前的交集、差集、并集等关系
'''

#复习列表,元祖创建
'''
a=[1,1,1,1,1]
b=list([1,2,3])
c=tuple([1,2,3])
d=(1,2,3)
'''
#1.集合创建 Set关键字
s=set('myname')  #重复只会保留一个  去重
print(s)  #{'n', 'y', 'm', 'e', 'a'} #m被去重

s1=['tom','jerry','eason','tom']
print(set(s1))  #{'eason', 'tom', 'jerry'}
#print(type(set(s1))) #<class 'set'>  set类型

#2.集合创建 必须元素是可哈希的 必须是：整形,字符串,元祖
#print(set((1,2)))

#3.set取值
tmp_set=set(s1)
print('tom' in tmp_set)  #判断元素是否粗存在。
tmp_set.add('jack')      #添加一个元素
tmp_set.update('lu')     #将字符串每一个元素都添加到集合中
tmp_set.update([19,'ela'])#添加多个元素  {'jack', 'jerry', 'tom', 'eason', 19, 'ela', 'l', 'u'}
print(tmp_set)






#4.集合分类：可变集合(可增删改查)、不可变集合

    #可变集合Set 可增删改元素,非可哈希的 不能作为字典的键，也不能做其他集合的元素

    #不可变集合frozenset 与上面相反

# num=[1,2,3]
# nset1=set(num)
# nset2=frozenset(num)
#
# print(nset1,nset2)  #{1, 2, 3} frozenset({1, 2, 3})


#5 删除集合
tmp_set.remove('jerry')
tmp_set.pop()  #随机删除 并返回被删除值
tmp_set.clear() #清空   set()
# del tmp_set
print(tmp_set)

print("_____________________________________________")

#集合操作符
#1. in  not in
#2. 比较访问符
print(set('driver')==set('drivererer'))
#3.包含不包含 <
print(set('teacher')<set('teacherael'))

#每一种集合 都有字符表达式可以代替

#交集intersection  有交集

a=set([1,2,3,4,5])
b=set([4,5,6,7,8])
print(a.intersection(b))  #{4, 5}
#print(a&b)

#反向交集         没有交集
print(a.symmetric_difference(b))  #{1, 2, 3, 6, 7, 8}
#print("反向交集",a ^ b)

#并集 union
print(a.union(b)) #{1, 2, 3, 4, 5, 6, 7, 8}
#print(a|b)

#差集  in a but  not in b
print(a.difference(b)) #{1, 2, 3}
#print(a-b)
#print(b-a)

#父集 超集
print( a.issuperset(b)) #a完全包含b a是父集
print(a>b)
#子集
print(a.issubset(b))
print(a<b)




