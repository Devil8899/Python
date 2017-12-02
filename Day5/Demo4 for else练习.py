#_author: liuz
#date: 2017/12/2

_user="liuz"
_pwd="pwd123"


#for  else
# 只要for循环正常执行完毕不被打断   就会执行else语句
for i in range(3):
    name=input("Username:")
    Pwd=input("Password:")
    if _user==name and _pwd==Pwd:
        print("登陆成功")
        passwd_authentication=True
        break  #跳出、中断  break for过后 就不会执行最后面的else语句
    else:
        print("用户名 或 密码 错误")
else:
    print("用户登录次数太多  用户锁定")
