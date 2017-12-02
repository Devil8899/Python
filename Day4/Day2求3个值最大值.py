#求输入3个值中 最大值和最小值
num1=int(input("Numer1:"))
num2=int(input("Numer2:"))
num3=int(input("Numer3:"))
Max_num=0
#定义一个第三方变量  通过两两比较
if num1 >num2 :
   Max_num=num1
   if Max_num >num3:
      print("最大值Max_num",Max_num)
   else :
      print("最大值Num3",num3)
else :
   Max_num=num2
   if Max_num >num3:
       print("最大值Max_num",Max_num)
   else :
      print("最大值Num2",num3)













#所有可能性
'''
if num1 > num2> num3  :
    print("最大值",num1)
elif  num1 > num3 > num2:
    print("最大值",num1)
elif num2 > num1 > num3 :
    print("最大值",num2)
elif num2 > num3> num1:
    print("最大值",num2)
elif num3 >num2 > num1 :
    print('最大值',num3)
elif  num3 > num1 > num2:
    print('最大值',num3)
else :
    print('比对失败')
'''