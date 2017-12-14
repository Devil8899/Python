#_author: liuz
#date: 2017/12/14
import  sys
sys.path.append("D:\\liuz\\new\\Python\\Day19\Demo3BASEDIR")  #解决方式 1. 通过将执行绝对路径写入环境中
from module import  main

#main.main()

#解决方案2   上面的方式移植环境 不能使用  通过下面方式获取上级上机的绝对路径 加入到环境中
import  os
print(os.path.abspath(__file__))  #返回path规范化的绝对路径
print(os.path.dirname(os.path.abspath(__file__))) #返回path的目录。其实就是os.path.split(path)的第一个元素
print((os.path.dirname(os.path.abspath(__file__)))) #通过这种方式就获取到上上级目录
#获取到了绝对路径
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
