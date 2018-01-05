#_author: liuz
#date: 2018/1/2
import pymysql
'''
存储过程是一个SQL语句集合，当主动去调用存储过程时，可以给变量赋值,查询结果集
其中内部的SQL语句会按照逻辑执行。
1、创建存储过程  在客户端创建
create procedure p1()
BEGIN
    select * from student;
END
call p1()  运行存储过程

2.创建有参数存储过程
对于存储过程，可以接收参数，其参数有三类：
in         仅用于传入参数用
out        仅用于返回值用
inout      既可以传入又可以当作返回值
1.定义参数 和参数类型
create procedure p2(
    in i1 int,
    in i2 int,
    inout i3 int,
    out r1 int
)
BEGIN
    DECLARE temp1 int;          #定义变量
    DECLARE temp2 int default 0;#定义变量
    set temp1 = 1;
    set r1 = i1 + i2 + temp1 + temp2; #返回类型的变量
    set i3 = i3 + 100;                #返回类型
end
调用
-- 执行存储过程
set @t1 =4;
set @t2 = 0;
CALL p2 (1, 2 ,@t1, @t2);
SELECT @t1,@t2;
创建后 在sql客户端上点击函数可以看到
'''
conn=pymysql.connect(host='localhost',user='root',password='qwe,123',database='scrapyspider')
coursor=conn.cursor() ## 创建游标



#在pymysql中调用 无参数存储过程
#1.创建存储过程
# try:
# #2.执行存储过程callproc()
#     coursor.callproc('p1')
# #3.查询数据库表中的所有行数据
#     result=coursor.fetchall()
#     print(result)
# except Exception as e:
#     print(e)


#调用有参数的存储过程  在客户端中执行 所有参数是分返回与不返回类型 但在python中 所有参数都会返回
# 执行存储过程,获取存储过程的结果集，将返回值设置给了  @_存储过程名_序号 =
r1 = coursor.callproc('p2', args=(1, 22, 3, 4))
print(r1) #(1, 22, 3, 4)
# result1 = coursor.fetchall()   #这个存储过程中 没有查询 所以返回Null元祖
# print(result1)

# 获取执行完存储过程的参数
r2 = coursor.execute("select @_p2_0,@_p2_1,@_p2_2,@_p2_3")  #获取存储过程所有参数
print(r2)
result2 = coursor.fetchall() #(1, 22, 103, 24)
print(list(result2))
conn.commit()


coursor.close()
conn.close()


