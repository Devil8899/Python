#_author: liuz
#date: 2017/12/11

#调用time 模块
import  time

#print(help(time))
#print(time.time())  #1512971407.5535803
#print(time.time()/60/60/24/365)

#time()                 #   *时间戳 返回当前时间的时间戳。
#print(time.clock())     #  *计算cpu执行时间

#print(time.gmtime())    #  结构化时间 和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time
#print(time.localtime()) #  结构化时间 本地时间   #time.struct_time(tm_year=2017, tm_mon=12, tm_mday=11, tm_hour=14, tm_min=14, tm_sec=50, tm_wday=0, tm_yday=345, tm_isdst=0)
#print(time.strftime('','')) #把一个代表时间的元组或者struct_time（如由time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。
#print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) #字符串时间********
#print(time.strptime("2017-12-11 14:14:50",'%Y-%m-%d %H:%M:%S'))#返回一个结构化时间
#time.struct_time(tm_year=2017, tm_mon=12, tm_mday=11, tm_hour=14, tm_min=14, tm_sec=50, tm_wday=0, tm_yday=345, tm_isdst=-1)

#times=time.strptime("2017-12-11 14:14:50",'%Y-%m-%d %H:%M:%S')
#print(times.tm_year,times.tm_mon,times.tm_wday) #tm_wday 一周的第几天

#把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。如果参数未给或者为None的时候，将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))。
#print(time.ctime(1304579615))

#将结构化时间转为秒
#print(time.mktime())  #将一个struct_time转化为时间戳。
#print(time.mktime(time.localtime()))

#time.sleep(secs)：线程推迟指定的时间运行。单位为秒。

#print(time.asctime())  #Tue Dec 12 09:39:35 2017
#另一个时间模块
import  datetime
print(datetime.datetime.now())  #2017-12-11 14:31:17.346349




'''
%a	本地（locale）简化星期名称	
%A	本地完整星期名称	
%b	本地简化月份名称	
%B	本地完整月份名称	
%c	本地相应的日期和时间表示	
%d	一个月中的第几天（01 - 31）	
%H	一天中的第几个小时（24小时制，00 - 23）	
%I	第几个小时（12小时制，01 - 12）	
%j	一年中的第几天（001 - 366）	
%m	月份（01 - 12）	
%M	分钟数（00 - 59）	
%p	本地am或者pm的相应符	一
%S	秒（01 - 61）	二
%U	一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。	三
%w	一个星期中的第几天（0 - 6，0是星期天）	三
%W	和%U基本相同，不同的是%W以星期一为一个星期的开始。	
%x	本地相应日期	
%X	本地相应时间	  
%y	去掉世纪的年份（00 - 99）	
%Y	完整的年份	
%Z	时区的名字（如果不存在为空字符）	
%%	‘%’字符

'''