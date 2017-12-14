#_author: liuz
#date: 2017/12/14

import  json
#用户对象
users={
    'id':100,
    'password':'abc',
    'credit':15000,
    'balance':15000,   #余额
    'enroee_date':'2019-02-01',  #注册时间
    'expire_date':'2019-02-02',  #到期时间
    'pay_date':19,
    'status':0  #0=use   1=locked  2=disabled
}
#序列化为字符串
print(type(json.dumps(users)))
with open('Accounts/Users','w') as file:
    file.write(str(users))  #这里没有序列化 通过转换 写入（必须是字符串）
#写入成功后 成功创建了一个用户对象