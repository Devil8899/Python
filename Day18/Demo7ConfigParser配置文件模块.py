#_author: liuz
#date: 2017/12/12

#configparser模块
#用于生成和修改常见配置文档，
# 当前模块的名称在 python 3.x 版本中变更为 configparser。

import configparser
#1.获取配置文件对象
config = configparser.ConfigParser()
'''
#2.通过字典方式进行存储
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}
config['bitbucket.org'] = {'User':'tom'}
config['topsecret.server.com'] = {}

topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
#3.写入文件 config.write()
with open('example.ini', 'w') as configfile:
    config.write(configfile)
'''

#读取配置文件内容 read()
#1.读取指定配置文件
config.read('example.ini')
#2.得到所有的section不包含DEFAULRT，并以列表的形式返回
#print(config.sections())
#3.获取DEFAULRT返回一个元祖
#print(config.defaults())
#4.判读是否存在
#print('topsecret.server.com' in config)
#5.取值 字典取值方式
#print(config['topsecret.server.com']['forwardx11'])

#for key in config['topsecret.server.com']:  #会默认把DEFAULT里面的键进行打印
 #   print(key)

#删除  重新写入
config.remove_section('topsecret.server.com')
#判断是否存在
#print(config.has_section('topsecret.server.com'))

#修改
config.set('bitbucket.org','user','jerry')
#删除子节点
config.remove_option('bitbucket.org','user')
#config.write(open('example.ini', 'w'))

'''
1.基本的读取配置文件

-read(filename) 直接读取ini文件内容

-sections() 得到所有的section，并以列表的形式返回

-options(section) 得到该section的所有option

-items(section) 得到该section的所有键值对

-get(section,option) 得到section中option的值，返回为string类型

-getint(section,option) 得到section中option的值，返回为int类型，还有相应的getboolean()和getfloat() 函数。

2.基本的写入配置文件

-add_section(section) 添加一个新的section

-set( section, option, value) 对section中的option进行设置，需要调用write将内容写入配置文件。

'''
