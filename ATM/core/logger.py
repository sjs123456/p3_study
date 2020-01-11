# !/usr/bin/env python
# encoding: utf-8

"""
@version: 
@author: sjs
@contact: ahusjs@163.com
@file: logger.py
@time: 2020/1/8 15:41
"""
import os
import sys
import logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from ATM.conf.settings import LOG_LEVEL,LOG_TYPES


def logger(log_type):
    logger = logging.getLogger(log_type)
    fh = logging.FileHandler(r'%s/log/%s'%(BASE_DIR, LOG_TYPES[log_type])) # 创建文件输出对象（输出到文件）
    ch = logging.StreamHandler() # 创建屏幕输出对象（输出到控制台）
    formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 创建输出格式对象（设置日志输出格式）
    fh.setFormatter(formater)  # 设置日志文件的输出格式
    ch.setFormatter(formater) # 设置日志控制台的输出格式
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.setLevel(LOG_LEVEL)  # 设置日志输出级别
    return logger


# logger('access').info('debug message')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logger.critical('critical message')