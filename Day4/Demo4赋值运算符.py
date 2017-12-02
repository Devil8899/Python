#赋值运算符
'''
+=  -=   *=  /=  
num += 1  等价于 num = num + 1
num -= 1  等价于 num = num - 1
num *= 2  等价于 num = num * 2
num /= 2  等价于 num = num / 2
num //= 2  等价于 num = num // 2   整除
num %= 2  等价于 num = num % 2     取余数  5%2 ..1
num **= 2  等价于 num = num ** 2   num=5  5*5 5的2次方
'''
num=1
num+=1  # 简写 ：num=num+1
print(num)
num2=10
num2-=2;# 简写  num2=10-2
print(num2)


#逻辑运算符
'''
and  not or

条件1 and 条件2  都为真则为true
条件1 or  条件2  有一个为真 则为真
not  不
not 5>3 ==false
not 5<3 ==true
具体 优先级不用记
短路原则
对于and 如果前面的第一个条件为假，
那么这个and前后两个条件组成的表达式 的计算结果就一定为假，
第二个条件就不会被计算

对于or 
如果前面的第一个条件为真，那
么这个or前后两个条件组成的表达式 的计算结果就一定为真，
第二个条件就不会被计算
(not (not True)) or (False and (not True))
true
'''