#输出长方形  根据输入 长宽，输出

width=int(input('width>>:'))   #用户输入宽度
height=int(input("height>>:")) #用户输入高度
#运用嵌套循环来
num =1
while num<=height:
    num2=1    
    while num2<=width:
        print("#",end="")   #不换行  
        num2+=1
    print()                 #换行
    num+=1

#注释版 
'''
height = int(input("Height:"))  # 用户输入一个高度
width = int(input("width:"))   # 用户输入一个宽度

#num2 = height

num2 = height  # 第一步： 赋值
while num2 > 0:   # 第二步 ：num2 == 2 

    num1 = width     # 第三步： 赋值
    while num1>0:   # 第四部：num1==2   # 第七步：num1 = 1 
        print("#", end="")  # 第五步： 不换行 打印一个#   第八步： 不换行 打印一个#
        num1 -= 1   #第六步： num1 = 1   第九步： num1 = 0
    print()  # 第十步 ： 只是换行
    num2 -= 1  # 第十一步 ： num2=1

##
##
'''