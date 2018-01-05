#_author: liuz
#date: 2017/12/28

import pymysql
'''
操作数据库的模块
pymysql   增删改查
mysqldb
'''
conn=pymysql.connect(host='localhost',user='root',password='qwe,123',database='scrapyspider')

## 连接mysql数据库并创建句柄 （host连接的机器，user连接的用户
# ，password连接的密=密码，database连接的数据库 ）


#1.插入excute、executemany  执行sq返回影响的行数
coursor=conn.cursor()
# name=input(">>")
#参数传递  多个参数使用元祖
# coursor.execute('insert into student(id,name,classname)VALUES (%s,%s,%s)',(name,'1','class1'))

#插入多条数据 2条
# list1=(
# (name,'class3'),
# (name,'class2')
# )
# r=coursor.executemany('insert into student(name,classname)VALUES (%s,%s)',list1)

#2.更新
#coursor.execute('update student set name="tony" where id=1')
#3.删除
#coursor.execute('delete from student where id=2')
#4.查  返回的数据是元祖类型
coursor.execute('select * from student')
result=coursor.fetchone() #fetchall() fetchmany() fetchone()
print(list(result))
result2=coursor.fetchone()
print(list(result2))

# coursor.scroll(-1,'relative')  #设置游标
result3=coursor.fetchone()
print(list(result3))

#获取自增id   lastrowid  返回当前插入行的的id
r=coursor.execute('insert into student(name,classname)VALUES (%s,%s)',('1','2'))
print(coursor.lastrowid)
conn.commit()  #提交 不然无法保存或新建修改的数据
conn.close()   #
'''
coursor=conn.cursor()  #游标用来取数据
##创建游标 ##查询数据库
row=coursor.fetchone()
##查询数据库表中的第一行数据
row_i=coursor.fetchmany()
# ##查询数据库表中的第(想要查询的)行数据  只能填写一个
row_d=coursor.fetchall()
# ##查询数据库表中的所有行数据
print(row)
##打印查询的数据内容（以元组的形式显示）
coursor.close()
##关闭游标执行操作
conn.close()
##断开连接
'''