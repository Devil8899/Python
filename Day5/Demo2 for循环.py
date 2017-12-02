#_author: liuz
#date: 2017/12/2

#打印3次  从0次开始  i代表临时变量 i=0  i+=1
'''
for i in range(3):  #range(3) = [0,1,2]  实际表示的意思
    print('loop:',i)
print("__________________________________")

for i in range(1,4):  #range(1,4) = [1,2,3]  实际表示是数组的意思
    print('loop:',i)
'''
# 打印1-100 所有奇数
'''
for i in range(1,101):
    if i % 2 == 1:
        print(i)
'''
# 打印1-100 所有奇数 使用步长 在range最后一个参数

#步长 这个技能很好用
'''
for i in range(1,101,2): #步长2  这样打印就是1,3,5 每次跨2步打印
    print(i)
'''
'''打印小于20 大于90'''
for i in range(100):
    if i<20 or i>90:
        print(i)