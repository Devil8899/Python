#_author: liuz
#date: 2017/12/5

#定义列表
'''
Menu=str({"北京市":{
          "东城区":{},
          "西城区":{},
          "崇文区":{}
            },"河北省":{
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
        }})
with open("ThreeList",'w',encoding='utf-8') as f:
    f.write(Menu)
'''
# Menu_list={}
with open('ThreeList','r',encoding='utf-8') as Fr:
     for line in Fr:
        Menu_list=eval(line)
        Menu_list2=Menu_list

tmp_list=[]
Is_Send=False
while True:
    with open('ThreeList', 'r', encoding='utf-8') as Fr:
        for line in Fr:
            Menu_list = eval(line)
            Menu_list2 = Menu_list
            Is_Send=False
        while not Is_Send:
            for key in Menu_list:
             print(key)
            choice=input("userChoiceJ>>")
            if choice in Menu_list:
             tmp_list.append(Menu_list)   #最后一个永远是父级
             Menu_list=Menu_list[choice]

            elif choice=="b":
             if tmp_list:                   #不为空 就是true
                Menu_list=tmp_list.pop()   #取到删除的最后一个值

            elif choice=="q":             #缩进级别 break是作用于while循环
                Is_Send=True
            elif choice=='w': #增
                choice2=input(">>")
                with open('ThreeList','w',encoding='utf-8')as fw:
                    Menu_list2[choice2]={}
                    fw.write(str(Menu_list2))
                print("写入成功")
                Is_Send=True
            else:print("无此项")






