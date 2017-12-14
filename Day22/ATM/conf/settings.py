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
