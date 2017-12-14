#_author: liuz
#date: 2017/12/14
#我这想使用模块下面  addmodel模块  因为环境变量中没有路径 所以手动加入
from sys import  path
path.append('D:\\liuz\\new\\Python\\Day19\模块')

#学习__name__  name变量 用来控制代码执行 可以判断代码是从哪里进行调用的
#__file__  变量返回当前文件绝对路径
#__name__  #__main__ 只有自己模块调用该代码 name=__main__  如果在别的模块调用该代码  __name__=被调用的模块文件名

import  addmodel

print(addmodel.add(19,2))

