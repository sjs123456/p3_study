# !/usr/bin/env python
# encoding: utf-8

"""
@version: 
@author: sjs
@contact: ahusjs@163.com
@file: settings.py
@time: 2020/1/8 16:17
"""

import os
import sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

DATABASE = {
    'engine':'file_storage', # suport mysql, postgresql,mongodb in the future
    'name':'accounts',
    'path':'%s/db' % BASE_DIR
}

LOG_LEVEL = logging.INFO

LOG_TYPES = {
    'transaction':'transaction.log',  # 交易日志
    'access':'access.log' #操作日志
}

TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.5},
    'transfor':{'action':'minus', 'interest':0.5},
    'consume':{'action':'minus', 'interest':0}
}

SUPER_ACCOUNT = {
    'sjs':'123456',
    'xh':'23456'
}
