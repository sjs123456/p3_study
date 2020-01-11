# !/usr/bin/env python
# encoding: utf-8

"""
@version: 
@author: sjs
@contact: ahusjs@163.com
@file: db_handler.py
@time: 2020/1/8 16:11
"""




def file_db_handler(con_param):
    """
    设置文件数据库的链接地址
    :param con_param:
    :return:
    """
    # print('file db')
    file_db_path = r'{0}/{1}'.format(con_param['path'], con_param['name'])
    return file_db_path

def mysql_db_handler():
    pass

def db_handler(con_param):
    """
    获取对应数据库的连接地址
    :param con_param: 数据库设置参数
    :return:
    """
    if con_param['engine'] == 'file_storage':
        return file_db_handler(con_param)
    elif con_param['engine'] == 'mysql':
        pass