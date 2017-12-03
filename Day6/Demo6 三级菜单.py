#_author: liuz
#date: 2017/12/3
Cun_City= {"北京市":{
          "东城区":{},
          "西城区":{},
          "崇文区":{}
            },
        "河北省":{
            "石家庄市":{
            "新乐市":{
                "apple":{}
            },
            "鹿泉市":{}
        },"唐山市":{
          "路南区":{}
        }
      ,"秦皇岛市": {
          "海港区":{
              "Lenove":{}
          }
            }
        }
    }

'''
对关键词  in  的运用  
in 就是看当前键   是不是在字典中   返回bool
以及for 循环的使用
在字典中for 循环  是循环的键  而在列表和元祖中则是下标

1.可以一层一层进入所有层
2.可以在每层返回上一层
3.可以在任意曾退出 主菜单 


'''


#标志位
Q_flag=False
#退出标志位
E_exit=False

while not Q_flag and not E_exit:
    for key in Cun_City:
        print(key)                 #一级菜单 省
    Choice=input("1>>:")
    if Choice in Cun_City:
        while not Q_flag and not E_exit:            #让程序停止在第二层
            for C in Cun_City[Choice]:
                print(C)                  #二级菜单
            choice2=input("2>>:")
            if choice2 == "b":
                Q_flag = True
            if choice2 == "q":
                E_exit = True
            if choice2 in Cun_City[Choice]:
                while not Q_flag and not E_exit:
                    for key3 in Cun_City[Choice][choice2]:
                        print(key3)
                    choice3 = input("3>>:")  #三级菜单
                    if choice3=="b":
                        Q_flag=True
                    if choice3 == "q":
                        E_exit = True
                    if choice3 in Cun_City[Choice][choice2]:
                        while not Q_flag and not E_exit:
                            for key3 in Cun_City[Choice][choice2][choice3]:
                                print(key3)
                            choice4=input("4>>:")
                            if choice4=='b':
                                Q_flag=True
                            if choice4=="q":
                                E_exit=True
                        else:
                            Q_flag=False
                else:
                    Q_flag = False
        else:
            Q_flag = False
