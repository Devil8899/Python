#_author: liuz
#date: 2017/12/11

#os模块

import  os
import time

print(os.getcwd()) #获取当前工作目录
#os.chdir(r'C:')   #修改路径
print(os.getcwd())
print(os.curdir)   #当前目录 .
print(os.pardir)   #父目录  ..
#print(os.makedirs('abc\dd'))     #创建目录文件夹   可生成多层递归目录
#print(os.removedirs('abc\dd'))   #删除多层文件夹    只能删除空文件
#os.mkdir('tset')
#os.remove(r'test\test2')         #删除单级空目录，若目录不为空则无法删除，报错

#print(os.listdir(r'D:\liuz\new\Python')) # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印 ['.git', 'Day14', 'Day15', 'Day16', 'Day17', 'Day18', 'Day3', 'Day4', 'Day5', 'Day6', 'Day7', 'Day8']
#print(os.remove('文件名'))        #只能删除文件 不能删除文件夹
#print(os.rename('oldname','newname'))  #重命名  文件或文件夹
#print(os.rename('test','testNew'))

os_info=os.stat('.\\os笔记')   #获取文件/目录信息
#print(os_info.st_size)         #大小
#print(os.sep)                 #os.sep    输出操作系统特定的路径分隔符  win下为"\\",Linux下为"/"
#print(os.linesep)            #os.linesep    输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
#print(os.pathsep)           #输出用于分割文件路径的字符串
#print(os.name)              #输出字符串指示当前使用平台。win->'nt'; Linux->'posix'

#print(os.system("dir"))  #运行shell命令，直接显示   相当于CMD执行
#print(os.environ)       #获取系统环境变量

#os.path.abspath(path)         返回path规范化的绝对路径
#print(os.path.abspath('os笔记'))  #D:\liuz\new\Python\Day18\os笔记

j=os.path.split(r'D:\liuz\new\Python\Day18\os笔记')  # 将path分割成目录和文件名二元组返回
#print(j)
#os.path.dirname(path)  返回path的目录。其实就是os.path.split(path)的第一个元素
#print(os.path.dirname(r'D:\liuz\new\Python\Day18\os笔记'))

#path.basename(path)>>>返回path最后的文件名。如果path以／或\结尾，那么就会返回空值。
## 即os.path.split(path)的第二个元素
#print(os.path.basename(r'D:\liuz\new\Python\Day18\os笔记'))

#path.exists(path)>>>如果path存在，返回True；如果path不存在，返回False
#print(os.path.exists("os笔记"))   #True

#path.isabs(path)>>>如果path是绝对路径，返回True
#print(os.path.isabs(r"..\.."))   #False

#如果path是一个存在的文件，返回True。否则返回False
#print(os.path.isfile("os笔记"))   #True

#path.isdir(path)>>>如果path是一个存在的目录，则返回True。否则返回False
#os.path.isdir('testNew')

#path.join(path1[, path2[, ...]])>>>将多个路径组合后返回，第一个绝对路径之前的参数将被忽略

#print(os.path.join(r"C:\file",'tmp\liuz'))  #C:\file\tmp\liuz

#path.getatime(path)>>>返回path所指向的文件或者目录的最后存取时间

#返回path所指向的文件或者目录的最后存取时间
print(os.path.getatime("os笔记"))
#返回path所指向的文件或者目录的最后修改时间
print(os.path.getmtime("os笔记"))

#print(time.ctime(1512984130.0482073))

def test():
    print("")
