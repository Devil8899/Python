#_author: liuz
#date: 2017/12/15
import os,sys,json
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from core import db_handler
from conf import settings

#重新获取用户数据
def load_current_balance(account_id):
    db_path =db_handler.db_handler(settings.DATABASE)
    account_file = '%s/%s.json' % (db_path, account_id)  # 打印对应用户文件
    with open(account_file, 'r')as file:
        print("读取文件里最新余额")
        account_data = json.load(file)
        return  account_data