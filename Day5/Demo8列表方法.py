#_author: liuz
#date: 2017/12/2

#列表的方法
#count('元素值')  计算列表某个元素出现的次数
a=['jerry','Jerry','jeams','eason','jack','Bryant']

#print(a.count('jerry'))
#print('sdjfk' in a)     不存在false

#extend(列表) 在源列表上合并2个列表
#x=[1,2,3]
#b=[4,5,6]
#x.extend(b)
#print(x+b)  #返回一个新的列表
#print(x)

#index('元素值')  返回索引
#print(a.index('jerry'))

#如何取列表重复值 列表没有提供 自己写
'''
c=['jerry','jack','jeams','eason','jack','Bryant']
first_index=c.index("jack")  #第一步 取第一个jack索引
Temp_list=c[first_index+1:]  #切片 取不包含第一个jack的列表到最后所有值
Sen_index=Temp_list.index("jack") #从第临时列表中 获取第二个jack索引
print(first_index+Sen_index+1)#因为排除了第一个jack的索引 所以+1
print(c[4]) #获取第二个jack的索引后  获取值
'''

#reverse  列表反转
#a.reverse()

#sort()  排序方法
#dj=[1,9,23,5,9]  #升序排序
#dj.sort()
#dj.sort(reverse=True)  #降序排序

#a.sort()        #字符串也可以排序  根据ASSIC码进行排序


'''

序号	函数
1	cmp(list1, list2)
比较两个列表的元素
2	len(list)
列表元素个数
3	max(list)
返回列表元素最大值
4	min(list)
返回列表元素最小值
5	list(seq)
将元组转换为列表

'''
'''
len([1, 2, 3])	3	长度
[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
3 in [1, 2, 3]	True       	元素是否存在于列表中
for x in [1, 2, 3]: print x,    	1 2 3	迭代

'''
