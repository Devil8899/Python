#_author: liuz
#date: 2017/12/21
from multiprocessing import Process,Manager
'''
不同进程之间使用共享数据
1.先Manager 创建一个实例
2.使用实例创建共享数据 比如 字典 列表
3.通过创建进程将共享数据传递到方法中进行使用 
4.子进程修改后主进程可以获取共享数据

'''
def f(d,l,i):
    d[i]='tom'   #只有这个会被覆盖
    # d['2']=2
    # d[0.25]=None
    l.append(i)
    # print(l)

if __name__=="__main__":
    #主进程创建  传给子进程使用
 with Manager() as manager:  #manager=Manager()
        d=manager.dict()         #字典
        l=manager.list(range(5)) #列表 0,1,2,3,4
        P_list=[]
    #创建10个进程
        for i in range(10):
            p=Process(target=f,args=(d,l,i))
            p.start()
            P_list.append(p)
        for res in P_list:
            res.join()
        print(d)
        print(l)
