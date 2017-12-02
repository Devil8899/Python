#猜名字游戏

name='jerry'
flag=True   #定义布尔类型  首字母大写
#break       终止循环

'''
while flag :
    User_name=input("name>>:")
    if  User_name==name:
        flag=False   #结束循环
        print("OK  you  are right")
    else:
        print("name is wrong")
'''
 
#break 使用
'''
num=1
while num<=10:
    print(num)
    num+=1
    
    if num==3:
        break
'''

#continue   跳出本次循环

'''
num2=0
while num2<=10:
    
    num2+=1
    if num2==5:
        continue
    print(num2)   #注意缩进级别
'''