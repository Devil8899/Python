#_author: liuz
#date: 2017/12/14

#1.
import logging,os,sys
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
#2.引用配置模块
from conf import  settings
def logger(logerType):
    loger2=logging.getLogger(logerType)
    loger2.setLevel(settings.LOG_LEVEL)  #设置日志输出级别  INFO
    #文件输出
    log_file='%s/log/%s'%(settings.BASE_DIR,settings.LOG_TYPES[logerType])
    fw=logging.FileHandler(log_file)
    fw.setLevel(settings.LOG_LEVEL)
    formaterNew = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    fw.setFormatter(formaterNew)
    #屏幕输出
    pm=logging.StreamHandler()
    pm.setLevel(settings.LOG_LEVEL)
    #添加2种输出
    loger2.addHandler(fw)
    loger2.addHandler(pm)

    return loger2  #返回logger对象
    #loger2.warning("sjkdf")


# logger('access')