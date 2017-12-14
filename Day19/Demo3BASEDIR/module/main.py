#_author: liuz
#date: 2017/12/14


#因为搜索路径 不是根目录 必须要将他们父路径加进去
import sys
#print(sys.path)
sys.path.append("D:\\liuz\\new\\Python\\Day19\Demo3BASEDIR")
from module import  logger

def main():
     logger.logging()
#main()