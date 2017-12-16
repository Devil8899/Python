#_author: liuz
#date: 2017/12/14
import os,sys,json,time
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from core import  db_handler
from conf import  settings

#登陆
def login(User,access_logger):
    ret_count=0
    if User['is_authenticated'] is not True  and ret_count<3:
        Account=input('UserAccount:>>')
        Password=input('UserPassword:>>')
        auth=Vail_user(Account,Password)
        if auth:
            User['is_authenticated']=True
            User['account_id']=Account
            return auth
        ret_count+=1
    else:
        access_logger.error(' login error  ')
        exit()  #退出整个程序


#验证
def Vail_user(Account,Password):
    db_path=db_handler.db_handler(settings.DATABASE)
    account_file='%s/%s.json'%(db_path,Account)  #打印对应用户文件
    print(account_file)
    if(os.path.isfile(account_file)):        #判断文件是否存在
        with open(account_file,'r')as file:
            data=file.read()
            account_data=json.loads(data)
            if account_data['Password']==Password:
                ex_time=time.mktime(time.strptime(account_data['expire_date'],'%Y-%m-%d'))
                if time.time()>ex_time:
                    print('时间过期')
                else:
                    return account_data          #登陆成功返回用户信息
            else:print('\33user login error')