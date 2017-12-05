#_author: liuz
#date: 2017/12/4


#更简单代码实现3级菜单


Menu={"北京市":{
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
        }}

current_layer=Menu;

parent_layer=[]               #动态循环保存所有父级,最后一个元素永远都是父亲级

while True:
    for Key in current_layer:
        print(Key)
    choice=input(">>")         #缩进级别 代表了choice 是在for循环后执行
    if choice in current_layer:
       parent_layer.append(current_layer)  #在进入下一层之前,把当前层(下一层的父级)追加进去
       #下一次循环 当用户选择b的时候 可以直接从列表取出最后一个值
       current_layer=current_layer[choice] #改成子层
    elif choice=="b":
        if parent_layer:  #列表不为空就是True
            current_layer=parent_layer.pop()   #pop不加参数代表删除最后一位，并返回  取出列表最后一位值
    else:print("无")
