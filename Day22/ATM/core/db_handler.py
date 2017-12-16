#_author: liuz
#date: 2017/12/15


import os,sys
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)


#判断验证方式
def db_handler(conn_parms):
    if conn_parms['engine']=="file_storage":
        return db_filehandler(conn_parms)
    # elif

#返回验证文本的路径
def db_filehandler(conn_parms):
    print('file_db文件验证 ',conn_parms)
    db_filepath='%s/%s'%(conn_parms['path'],conn_parms['name'])  #拼接验证文件路径字符串
    return  db_filepath
