#_author: liuz    默认当前系统用户  设置-文件和代码模板
#date: 2017/12/2

#学习内容 ：1.格式化输出
'''
2.学习了数据类型   数字    int  float
                 布尔    Bool
                 字符串  str
'''
# 占位符 %s

name=input("Name>>:")
age=int(input("Age>>:"))    #转为数字
job=input("Job>>:")
salary=input("Salary>>:")   #工资 浮点数
#print(name,age,job,salary)

#如果想输出这种格式 要通过占位符来创建
# #同时变量和占位符一一对应

if salary.isdigit():          #判断是不是数字
    salary=int(salary)
else:
    exec("must input digit")  #如果不是退出程序

msg='''
-------- nfo of %s  -----
Name: %s
Age : %d   
Job : %s
Salary: %f
You will be retired in %s years
---------- end -----------------
'''  %(name,name,age,job,salary,65-age)   #变量和占位符一一对应

print(msg)



''' 
 占位符 %s  s = string
       %d  d = digit 整数
       %f  f = float 浮点数，约等于小数
 占位符指出了数据类型，变量在传值时必须也要是相应类型
'''