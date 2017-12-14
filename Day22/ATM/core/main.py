#_author: liuz
#date: 2017/12/14


#定义主函数
#功能  1.登陆功能
from core import auth,logger



'''
初始化用户
'''
User_data={
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}
#定义日志  获取到logger对象
access_logger=logger.logger('access')
trans_logger=logger.logger('transaction')

def run():
    auth.login(User_data,access_logger)



