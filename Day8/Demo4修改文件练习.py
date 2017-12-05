#_author: liuz
#date: 2017/12/5

#修改文件？  只能在替换文件中进行修改 不能在一个文件中实现修改

#既可读又可写
f=open("Usertxt",'r+',encoding='utf=8')
fw=open('UserWrite','w',encoding='utf-8')

number=0
for line in f:
    number+=1
    if number==1:
        line='替换成新的 \n'
    fw.write(line)
fw.close()
f.close()

