# _author: liuz
# date: 2017/12/2

#1.列表

#1.1定义列表
a=['jerry','tom','jeams','eason','jack','Bryant']

#1.2增删改查

 #取值  通过下标  下标从0开始
 #print(a[3])

 #增 切片 取值范围   遵从左包括，右不包括

 #第二个参数代表取值范围
 #最后一个参数 代表步长
 #print(a[1:4])   #['tom', 'jeams', 'eason']
 #print(a[1:])    #空，取值范围从tom到最后一个
#print(a[1:-1])  #-1 代表取值到最后倒数第二个值

#print(a[:-1])   #从开始到倒数第 二个
 #列表也有步长
#print(a[1::1])#从左到右一个一个取

#如果想隔着取值 可以设置步长
#print(a[1::2]) #从左到右隔一个取值  ['tom', 'eason', 'Bryant']

#从右往左取值 倒过来取值
#print(a[3::-2])  #['eason', 'tom']
#从索引3到最后取值   -2 负数代表了方向到右边  代表了方向
# 索引3作为右边第一个 隔一个开始取值
#print(a[3::-1]) #从eason到右边最后 依次取值
#print(a[3:1:-1])#['eason', 'jeams']  从索引3到右边取一个
#print(a[-2::-1])#倒数第二个到最后

#添加 append insert
#a.append('tony')#默认插到最后一个位置
#a.insert(1,'Pony')#插入到第二个位置  可以指定索引 插入到任意位置
#print(a)


#修改
#a[0]="jack"
#a[1:3]=['a','b']  #批量修改 多个值


#删除 remove pop del

#a.remove('Bryant') #直接跟移除的值  不要下标
#name=a.pop(1)  #根据下标删除  并且返回被删除的值
#del a[0]  #根据下标删除
#del a    #将a 对象删除


