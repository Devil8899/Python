#_author: liuz
#date: 2017/12/14

import  logging,os,re
#设置日志级别
LOG_LEVEL=logging.INFO
#路径
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#日志类型
LOG_TYPES={
    'access':'access.log',
    'transaction':'transaction.log'
}

#定义验证数据库
DATABASE={
    'engine':'file_storage',
    'name':'Accounts',
    'path':'{basedir}/db'.format(basedir=BASE_DIR)
}

#存取款类型
TransType={
    'repay':{'action':'plus','interset':0},      #付款
    'withraw':{'action':'minus','interset':0.05},
    'transfer':{'action':'minus','interset':0.05},
    'consume':{'action':'minus','interset':0}
}