#_author: liuz
#date: 2017/12/2
#
a,b=[2,3]
#实际 a=2 b=3


#商品列表
product_list=[
    ('Mac',9000) , #不可修改  使用元祖
    ('Kindle',8000),
    ('tesla',900000),
    ('PythonBook',105),
    ('Pc',9000),
]
#str.isdigit() 方法检测字符串是否只由数字组成。
Money=input('please input your Money:')

Shop_list=[]
if Money.isdigit():
    Money=int(Money)

    while True:
   #enumerate 默认从0开始 设置从1开始
   #变量v  使用了2个变量来接受  i=序号 v=元祖
        for i, v in enumerate(product_list, 1):
            print(i, '  ', v)
        choice = input("输入商品列表编号[退出:q]")
        if choice.isdigit():
            choice=int(choice)
            if(choice>0 and choice<len(product_list)):
                product= product_list[choice-1]               #取单个商品
                if product[1]<=Money:
                    Shop_list.append(product[0])
                    Money-=product[1]
                    print("购买成功",product[0],'余额',Money)
                else:
                    print("余额不足",Money)
        elif choice == "q":
               for i in Shop_list:
                   print("购买了",i)
        else:
                print("输入编号不正确")


else:
    print('输入是非法字符')

