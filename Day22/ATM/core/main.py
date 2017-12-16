#_author: liuz
#date: 2017/12/14


#定义主函数
#功能  1.登陆功能
import os,sys
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from core import auth,logger,accounts,transtion



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
#access_logger.info('123')



#菜单展示
def interactive(Userdata):
    menu='''
    _______________欢迎你,%s___________________
    1.账户信息
    2.存款
    3.取款
    4.转账
    5.账单
    6.退出
    '''%(Userdata['account_data']['id'])
    menu_dic={'1':accout_info,
          '2':repay,
          '3':withdraw,
          '4':transfer,
          '5':pay_check,
          '6':'logout'
          }
    exit_flage=False
    while not exit_flage:
         print(menu)
         choice=input(">>").strip()
         if choice in menu_dic:
            menu_dic[choice](Userdata)


def accout_info(Userdata):
    print(Userdata)

#存款
def repay(Userdata):
    accountNew= accounts.load_current_balance(Userdata['account_id'])
    current_balance='''-------Balance_Info-------
     银行金额：%s
     银行余额: %s
    '''%(Userdata['account_data']['credit'],Userdata['account_data']['balance'])
    print(current_balance)
    back_flage=False
    while not back_flage:
        repay_amount=input("repay amount>>")
        if len(repay_amount)>0 and repay_amount.isdigit():
         new_balance=transtion.transtion(trans_logger,accountNew,'repay',repay_amount)
         if new_balance:  #如果有返回值
             print('用户%s您最新银行余额%s'%(str(new_balance["id"]),str(new_balance["balance"])))


def withdraw(Userdata):
    print()
def transfer(Userdata):
    print()


def pay_check(Userdata):
    print()

def logout(Userdata):
    print()



#主程序
def run():
    ac_data=auth.login(User_data,access_logger)
    if(User_data['is_authenticated']):
        User_data['account_data']=ac_data
        interactive(User_data)

#run()