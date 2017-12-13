#_author: liuz
#date: 2017/12/11

#随机数模块
import  random

#0-1随机数
#print(random.random())
#返回1-8 随机整数
#print(random.randint(1,8))         #包含8
#返回随机一个字符                                  *************
#print(random.choice('hellojerry'))
# choice方法返回一个列表，元组或字符串的随机项。
print(random.choice(['hellosjd',4,[1,2]]))

#shuffle(可以是一个序列或者元组) 方法将序列的所有元素随机排序。

list2 = [20, 16, 10, 5];
random.shuffle(list2)
#print("随机排序列表 : ",  list2)

##sample(seq, n) 从序列seq中选择n个随机且独立的元素；
#print(random.sample(list2,2))

#randrange(start,stop,step) 方法返回指定递增基数集合中的一个随机数
'''
start -- 指定范围内的开始值，包含在范围内。
stop -- 指定范围内的结束值，不包含在范围内。
step -- 指定递增基数。
'''
#print(random.randrange(1,3))

# 输出 100 <= number < 1000 间的偶数
#print("randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2))


#验证码

def getCode(m):
    code=''
    for i in range(m):
        code_tmp=random.randrange(0,10)                #数字
        Code_e=chr(random.randrange(65,91))            #字母  在ASSIC中 65-91存英文
        code="".join([str(code_tmp),Code_e,code])
    print(code)

#getCode(3)
def getcode2(m):
    code=''
    for i in range(m):
        tmp_code=random.choice([random.randrange(1,10),chr(random.randrange(65,91))])
        code+=str(tmp_code)
    print(code)
#getcode2(5)