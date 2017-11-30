#用户交互  捕捉用户输入 类似与java与C#中控制台输入
name=input("your name")  
age=input("your age")  #input 接收的所有数据 都是字符串  即便你输入数字  
#print(name,age)
books=input("book")

Sunage=100;
#数据类型 转换
# int interger =整数   字符串转int,用int( 被转数据)
# str string =字符串   把数据转成字符串str(被转数据)
print("your name and age ",name,age)
print("____________________________________________")
print("总后100本还有多少本",Sunage-int(books),'书');  # 逗号隔开是不同的语句 不用类型转换为字符串
print("总后100本还有多少本"+str(Sunage-int(books))+'书');
 #要将运算的结果转为字符串 不然拼接会报错