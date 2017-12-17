#_author: liuz
#date: 2017/12/17
#利用属性实现分页
class pageInfo:

    def __init__(self,Cur_page):
        self.page=int(Cur_page)
    #定义属性
    @property
    def start(self):
        val=(self.page-1)*10
        return val
    @property
    def end(self):
        val=self.page*10
        return val


li=[]
for i in range(10000):
    li.append(i)

while True:
    Cur_page=input("输入页码")
    cur=pageInfo(Cur_page)
    print(li[cur.start:cur.end])