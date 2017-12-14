#_author: liuz
#date: 2017/12/14

#一个.py文件就称之为一个模块
'''
模块分为三种
1.python标准库  如 re正则
2.第三方库
3.自己定义模块
'''
'''
包的概念：
Python引入了目录结构的概念  防止同名冲突  包用来组织模块
右击新建 PythonPackage包  里面默认有一个_init_.py文件
'''



import sys
#1.import 模块名
# import  addmodel  #通过搜索路径找到addmodel.py文件    解释了文件中所有代码
# print(addmodel.sub(10,2))

# #2.from  关键字 只调用模块里面的add方法 作为本地方法来运行
# from addmodel import  add,sub
# print(add(1,2))

#3. *  代表引入了addmodel模块所有方法  不用加模块名.方法名调用
#from addmodel import *
# def sub2(x):
#     print(x,"hhh")
# sub2('123')   #存在同名情况  会被覆盖掉

#4.as关键字 给方法起别名 通过别名调用方法
from addmodel import  add as add1
#print(add1(1,239))

#_____________________________________________________________________________

#调用包下面的模块  from  包名 import 模块名
from Firlogger import M_Print
#M_Print.print2()
#调用包里面嵌套包 M_file模块
#from Firlogger.Senlogger import  M_file
#M_file.file()

#调用包下面模块下面的方法    方法就能通过方法名调用了
from Firlogger.Senlogger.M_file import file
#file()


#直接调用包
import Firlogger  #会执行——init——.py文件


