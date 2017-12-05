#_author: liuz
#date: 2017/12/5

#f=open('Usertxt','a',encoding='utf-8')

#进度条效果  flush立刻刷新
'''
import  sys,time
for i in range(30):
    print('*',end='',flush=True)
    time.sleep(0.2)
'''

#截断方法
#runcate() 方法用于截断文件，
# 如果指定了可选参数 size，
# 则表示截断文件为 size 个字符。
#  如果没有指定 size，则从当前位置起截断；
# 截断之后 size 后面的所有字符被删除。
#f.truncate(6) #从6个字符 就是2个汉字后开始截断


#文件的其他方法。。。。。。

#r+ 模式  读+写
'''
f=open('Usertxt','r+',encoding='utf-8')
for i in range(4):
    print(f.readline())
# f.write("最能追加到最后了")
f.close()
'''

#w+ 模式 写加读  w写入会先清空
'''
fw=open('Usertxt','w+',encoding='utf-8')
fw.readline()
fw.write("写入了吗")
fw.seek(0)
print(fw.readline())
'''

#a+ 追加 默认光变在最后一个开始追加
'''
fa=open('Usertxt','a+',encoding='utf-8')
fa.readline()
print(fa.tell())
fa.write("123 \n")
print(fa.tell())
fa.close()
'''




