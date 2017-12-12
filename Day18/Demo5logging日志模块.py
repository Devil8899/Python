#_author: liuz
#date: 2017/12/11

#日志模块

import logging
'''
很多程序都有记录日志的需求，并且日志中包含的信息即有正常的程序访问日志，
还可能有错误、警告等信息输出，
python的logging模块提供了标准的日志接口，
你可以通过它存储各种格式的日志，
logging的日志可以分为 debug(), info(), warning(), error() and critical() 
5个级别，
'''



#日志基本配置basicConfig()默认日志显示级别，
logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s%(message)s',  #括号内都是变量
        datefmt='%m/%d/%Y %I:%M:%S %p',  #asctime定义时间格式
        #filename='tmp/test.log',
        #filemode='a'  #可以不用指定 默认是a
                    )

# logging.debug('1')
# logging.info("2")
# logging.warning("3")
# logging.error("4")
# logging.critical("5")
#12/11/2017 10:03:31 PM Demo5logging日志模块.py[line:25]DEBUGdebug
#五种级别全部写入文件

#basicConfig() 参数：
#filename  日志所存文件名
#filemode  文件模式  w 创建写入/存在覆盖  a 追加
#如果不写filename 默认就是打印
#datefmt:指定日期时间格式
#format:制定handle使用的日志显示格式
#level 设置日志级别








