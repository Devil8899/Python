#_author: liuz
#date: 2018/1/3
import pymysql

#事物一般定义在存储过程中
'''
create PROCEDURE p1(   #定义存储过程
    OUT p_return_code tinyint
)
BEGIN 
  DECLARE exit handler for sqlexception   #定义报错调用的方法
  BEGIN 
    -- ERROR 
    set p_return_code = 1; 
    rollback; 
  END; 
 
  DECLARE exit handler for sqlwarning    #定义报错调用的函数
  BEGIN 
    -- WARNING 
    set p_return_code = 2; 
    rollback;                            #回滚
  END; 
 
  START TRANSACTION;                     #定义事物 start transaction 
    DELETE from tb1;
    insert into tb2(name)values('seven');
  COMMIT;                                #提交事务 报错会执行上面异常对应的方法
 
  -- SUCCESS 
  set p_return_code = 0; 
 
  END
'''