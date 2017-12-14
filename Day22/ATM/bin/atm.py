#_author: liuz
#date: 2017/12/14

import  os,sys
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
# D:\liuz\new\Python\Day22\ATM 这样就可以在当前环境中引用core这个ptyon包里面的模块和方法了
#1.调用core包下main模块
from core import main

#2.调用main模块下面的run()方法
main.run()