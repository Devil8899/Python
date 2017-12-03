#_author: liuz
#date: 2017/12/3

# 1.定义3级省  市  县 字典
'''
Cun_city={
    '省':{
        '市':['县']
         }
    }
'''
Cun_City= [
  {
    "name": "北京市",
    "city": [
      {
        "name": "北京",
        "area": [
          "东城区",
          "西城区",
          "崇文区",
          "宣武区",
          "朝阳区",
          "丰台区",
          "石景山区",
          "海淀区",
          "门头沟区",
          "房山区",
          "通州区",
          "顺义区",
          "昌平区",
          "大兴区",
          "平谷区",
          "怀柔区",
          "密云县",
          "延庆县"
        ]
      }
    ]
  },
  {
    "name": "河北省",
    "city": [
      {
        "name": "石家庄市",
        "area": [
          "新乐市",
          "鹿泉市"
        ]
      },
      {
        "name": "唐山市",
        "area": [
          "路南区",
          "路北区",
          "古冶区",
          "开平区",
          "新  区",
          "丰润县",
          "滦  县",
          "滦南县",
          "乐亭县",
          "迁西县",
          "玉田县",
          "唐海县",
          "遵化市",
          "丰南市",
          "迁安市"
        ]
      },
      {
        "name": "秦皇岛市",
        "area": [
          "海港区",
          "山海关区",
          "北戴河区",
          "青龙满族自治县",
          "昌黎县",
          "抚宁县",
          "卢龙县"
        ]
      }]
  }]

print('----------------全国省市县%s----------' % '选择列表')  # 复习格式化

for i in Cun_City:
    print(i["name"])
print('{end}'.center(50, '-').format(end='ending'))  # 居中显示 +  字符串格式化

# 3.获取输入

#标志位
leael='省'


while True:
    # 2.打印 3级菜单
    UserChoic = input("输入您选择的>>")
    # 4.1 根据输入的省市 展示菜单
    for i in Cun_City:
        if UserChoic==i["name"]:                    #获取省名
            City_list=i['city']
            for j in City_list:
              print(j["name"])

        else:
            City_list = i['city']
            for j in City_list:
                if UserChoic==j["name"]:
                   Xian_list=j['area']
                   for x in Xian_list:
                       print(x)

    # 4.2 输入  返回  返回上级菜单
    if UserChoic=="t":
        break



    # 4.3 输入q 推出程序
    if UserChoic=="q":
        print("您选择了推出程序")
        break