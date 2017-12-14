#_author: liuz
#date: 2017/12/11

#logger是一个模块级别的函数

#1.引用模块  获取logger对象
import  logging
logger2=logging.getLogger()
# logger1=logging.Logger('logname',level=logging.DEBUG)

#2.创建handler(文件输出流),写入日志文件 文件对象
fw=logging.FileHandler("test.log")

#3.再创建一个handler，用于输出到控制台  屏幕输出对象
ch=logging.StreamHandler()

#4.定义格式
formaterNew=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

#5.给文件和屏幕输出定义格式
fw.setFormatter(formaterNew)
ch.setFormatter(formaterNew)

#实现输出方式
logger2.addHandler(fw)
logger2.addHandler(ch)
#设置级别 DEBUG 为最低 就能把全部五种级别全部打印
logger2.setLevel(logging.DEBUG)

#默认只能打印warning或者级别更高的
logger2.debug("logger debug message")
logger2.info("logger info message")
logger2.warning("logger warning message")


