#_author: liuz
#date: 2017/12/8

#函数参数

def PrintName(age,name,sex='man'): #1.参数默认值 sex='男'  必须放在参数列表最后
    print("年纪%s"%age)
    print("名字%s"%name)
    print("性别%s"%sex)


#PrintName(90,'peng','wman')
print("_________________________________________________________________________")
#2.通过位置参数调用  在C#也有
#PrintName(name='zu',age=100)

#3.传入多个参数 不定长参数  *参数名  一般使用args
def adds(*args):    #以元祖来存多个参数 args=(10, 20)
    num=0
    for i in args:  #循环元祖
        num+=i
    print(num)

#adds(10,20)
#adds(10,20,30)

#4.传入多个参数  但参数是有名字的  使用**参数名接收  一般使用kwargs
def Users(*args,**kwargs):  #以字典形式来存  必须放最后边
   print(kwargs)#{'address': 'shanghai', 'name': 'jerry', 'age': '18'}
   print(args) #('driver', 'teacher')
   for key in kwargs:                             #for循环  遍历列表、元祖是下标  遍历字典是代表字典中的一个元素
       print(key,kwargs[key])

#Users('driver','teacher',name="jerry",age='18',address='shanghai')
#Users(name="jerry",age='18',address='shanghai') #有命名参数 通过 key:value传值  #传了一个空元祖


#5.位置关系
#关于不定长参数 *args放左边  **kwargs放右边
# 如果有默认参数 放左边
def addUser(sex='man',*args,**kwargs):
    print(args)
    print(kwargs)

addUser('wan',1,2,3,name='tom')