name=input("name >>:")
pwd=input("pwd >>:")

nam2="tom"
pwd2="123"
num="1"
     file_object2 = open('data.txt')   #read 打开文件
try:
     all_the_text = file_object2.read( )   #读取数据
finally:
     file_object2.close( )   #关闭资源
if name==nam2 and pwd==pwd2:
    print("登陆成功")
elif all_the_text=="3":                      #输入3次错误,锁定
    print("用户锁定")
elif all_the_text=="":                        #第一次 读取数据是空
    print("登陆失败 请再次输入用户名密码")
    file_object = open('data.txt', 'w')   
    file_object.write(num);                   #写入1
    file_object.close()                       #关闭资源
elif all_the_text=="1":                       #第二次   如果是1
    print("登陆失败 请再次输入用户名密码")
    file_object = open('data.txt', 'w')
    file_object.truncate()
    file_object.write(str(int(all_the_text)+1));   #写入2
    file_object.close()
elif  all_the_text=="2":                           #第三次
    print("登陆失败 请再次输入用户名密码")
    file_object = open('data.txt', 'w')
    file_object.truncate()
    file_object.write(str(int(all_the_text)+1));   #写入3
    file_object.close()