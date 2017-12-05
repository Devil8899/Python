# _author: liuz
# date: 2017/12/5

# f=open('Usertxt').read()

# 读取数据
'''
fread=open("Usertxt",'r',encoding='utf-8')
#参数
#r 代表读
#w代表写     覆盖 encoding 代表读取的格式
#a 代表追加  不覆盖
data=fread.read(5)
print(data)
#read(参数)   参数： 读取的字符个数
fread.close()
'''


#写
# 写入文件  如 果没有找到文件就会创建文件
# 如果有文件内容 则会被覆盖
# 如果不写入 文件内容也会被清空


fwrite = open('Usertxt', 'w', encoding='utf-8')
# fwrite.fileno()
fwrite.write('writetest')
fwrite.write('123')          #多次写入默认不换行
fwrite.close()

#追加  不存在创建文件
fappend=open("Usertxt",'a',encoding='utf-8')
fappend.write('append内容')
fappend.close()

#close()  python会自动释放资源 但是不可靠