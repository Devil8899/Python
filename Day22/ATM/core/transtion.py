#_author: liuz
#date: 2017/12/15
import os,sys,json
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from conf import settings
from core import db_handler
def transtion(logger,account,actionD,money,**other):
     money=float(money)
     if actionD in settings.TransType:
        #计算利息
        interest=money * settings.TransType[actionD]['interset']
        oldbalance=account["balance"]
        if settings.TransType[actionD]["action"]=="plus":
            newbalance=oldbalance+money+interest
        elif settings.TransType[actionD]["action"]=="minus":
            newbalance=oldbalance-money-interest
            if newbalance <0:
                print("金额超出")
                return
     account["balance"]=newbalance
     dump_account(account)
     logger.info("完成银行操作")
     return account

#重新写入
def dump_account(account):
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = '%s/%s.json' % (db_path,account["id"] )  # 打印对应用户文件
    with open(account_file, 'w')as file:
        print("写入文件里最新余额")
        data=json.dumps(account)
        file.write(data)
        print("写入成功")
        return  True