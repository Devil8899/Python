#_author: liuz
#date: 2017/12/2

#for循环练习
#for  else 只要for循环正常执行完毕不被打断   就会执行else语句
_user="liuz"
_pwd="pwd123"

passwd_authentication=False   #flag 标志位

for i in range(3):
    name=input("Username:")
    Pwd=input("Password:")
    if _user==name and _pwd==Pwd:
        print("登陆成功")
        passwd_authentication=True
        break
#跳出、中断  break for过后 就不会执行最后面的else语句
    else:
        print("用户名 或 密码 错误")
#if not passwd_authentication:  #当为真的情况执行
 #   print("登陆次数过多,不能再进行登陆")

else:   #和执行标志位的结果一致
    print("登陆次数过多,不能再进行登陆")


# 复习逻辑运算符  and 和 or 或  not 不