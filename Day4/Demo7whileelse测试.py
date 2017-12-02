#while else
#在 python 中，while … else 在循环条件为 false 时执行 else 语句块：

'''
num=0
while num<5 :
    print(num)
    num+=1
else:
    print('条件不成立了')
'''

'''  输出结果
0
1
2
3
4
条件不成立了
'''

#为末尾end传递一个空字符串，这样print函数不会在字符串末尾添加一个换行符，而是添加一个空字符串
print('sayhi',end="")  #一行内显示  或者使用 \n 换行符  \r 当前行第一个位置 window中使用多
print('sayhi',end="")  #
print('sayhi',end="")
print()  #默认会换行  等价于 print(end="\n")  
