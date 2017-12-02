#_author: liuz
#date: 2017/12/21

#购物车练习

#1.输入工资
salary=input("输入你的工资>>:")
#2.维护商品列表
goods_list=[[1,'iphone8',8000],[2,'Nokia',6000],[3,'ipod',1000],[4,'Macbook',20000],[5,'Mobile',1500]]
#3.打印商品列表
if salary.isdigit():  #str.isdigit() 方法检测字符串是否只由数字组成。
    salary=int(salary)
    for goods in goods_list:
        Ttmp_goods=goods
        msg = '''序号:%d  品牌:%s  价格：%d ''' % (int(Ttmp_goods[0]), str(Ttmp_goods[1]),int(Ttmp_goods[2]))
        print(msg)
else:
    print('工资输入是非法字符')
#5.定义购买列表
Purchase_list=[]   #购买的列表

#6.执行循环购买
while salary > 0:
    Tmp_num = input('请输入购买的商品列表[退出:quit]>>:')
    if Tmp_num== 'quit':                              #判断退出
            print('欢迎再次购买'+'您购买了',Purchase_list)
            break
    if str(Tmp_num)=="":
            print('列表不能为空')
    if Tmp_num.isdigit():
            for  goods in goods_list:
                goods_num=goods[0]            #取出单个商品
                if goods_num==int(Tmp_num):
                        goods_Price=goods[2]  #取出单个商品价格
                        if goods_Price<=salary:
                            salary-=goods_Price    #还剩的钱=工资-商品价格
                            print("加入购物车",goods[1],'成功'+'当前余额',salary)
                            Purchase_list.append(goods[1]+'价格:'+str(goods[2]))  #加入购买列表
                            break
                        else:
                            print('余额不足',salary-goods_Price)
                            break               #跳出 防止for还要执行循环

            else:
                print('没有找到对应商品')
    
        



