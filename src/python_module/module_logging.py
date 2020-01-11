# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : sjs

# 日志
import logging


# 可以进行日志添加和输出(只能取一种)
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt = '%a,%d %b %Y %H:%M:%S',filename='test.log',filemode='w'
#                    ) #
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

logger = logging.getLogger()
fh = logging.FileHandler('test.log') # 创建文件输出对象（输出到文件）
ch = logging.StreamHandler() # 创建屏幕输出对象（输出到控制台）
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 创建输出格式对象（设置日志输出格式）
fh.setFormatter(formater)  # 设置日志文件的输出格式
ch.setFormatter(formater) # 设置日志控制台的输出格式
logger.addHandler(fh)
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)  # 设置日志输出级别

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')