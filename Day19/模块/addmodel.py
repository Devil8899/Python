#_author: liuz
#date: 2017/12/14

#自己定义模块

#print("_________________________________ok_____________________________________")
def add(x,y):
    #print("this is add")
    return x+y

def sub(x,y):
    return x-y

def sub2(x):
    print(x)

if __name__=='__main__':
    print(add(10,20))

print('__name__',__name__)  #__main__ 作为自己文件调用 name=__main__  如果在别的模块调用 __name__=执行的模块文件名