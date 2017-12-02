#_author: liuz
#date: 2017/12/2
_user="liuz"
_pwd="pwd123"

#右单机断点调试
#while else 当while不为true时最后会执行else语句
counter=0

while counter<3:
    name = input("Username:")
    Pwd = input("Password:")
    if _user == name and _pwd == Pwd:
        print("welcome",name)
        break
    else:
        print("登陆错误")
    counter+=1
    if counter==3:
        Num_custmer=input("try again[yes/no]?")
        if Num_custmer=='yes':
            counter=0
else:
    print("用户次数过多,程序退出")