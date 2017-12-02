#99乘法表  使用while循环
'''
1*1
1*2 2*2
1*3 2*3 3*3
'''
'''
num=1
while num<9 :
    temp=num
    while temp>0 :
        print('*',end='')  #不换行
        temp-=1
    print()
    num+=1
'''

#9*9 乘法表
first=1
while  first<=9:
    temp=1
    while temp<=first :
        print(temp,'*',first,'=',temp*first,end=' ')  #不换行
        temp +=1
    print()
    first+=1


print('______________________________________________________________________________')
#9*9倒序
Seo=9
while Seo>0:
    tmp=1
    while tmp<=Seo:
        print(tmp,'*',Seo,'=',tmp*Seo,end='\t')  #'\t' 制表符
        tmp+=1
    print()
    Seo-=1

