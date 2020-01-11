# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : sjs

import configparser

config = configparser.ConfigParser()
#写入配置信息
# config['DEFAULT'] = {
#     'serverAliveInerval':45,
#     'Compression':'yes',
#     'CompressionLevel':'9'
# }
# config['bitbucket.org'] = {'user':'hg'}
# config['topsecret.server.com'] = {
#     'Host Port':'50022',
#     'Forwordx11':'no'
# }
# config['DEFAULT']['Forwardx11'] = 'yes'
#
# with open('example.ini', 'w') as configFile:
#     config.write(configFile)

# 获取配置文件的信息
# config.read('example.ini')
# print(config.sections())
# print(config.defaults())
# print('bytebong.com' in config)
# print('bitbucket.org' in config)
# print(config['bitbucket.org'])
# for key in config['bitbucket.org']:
#     print(key)  # 打印出当前模块和默认模块下的文件
# print(config.options('bitbucket.org'))   # 同for循环,找到'bitbucket.org'下所有键
# print(config.get('bitbucket.org', 'compression')) # yes       get方法取深层嵌套的值
# print(config.items('bitbucket.org'))  #找到'bitbucket.org'下所有键值对


# 增删改
config.read('example.ini')
# config.remove_section('bitbucket.org')
# config.add_section('alex')
# print(config.has_section('bitbucket.org'))
# config.set('yuan', 'k', 'kk')


config.write(open('example.ini', 'w'))  # 最后一步，进行增删改再重新写入文件