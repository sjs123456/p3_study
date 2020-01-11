# !/usr/bin/env python
# encoding: utf-8

"""
@version: 
@author: sjs
@contact: ahusjs@163.com
@file: account_sample.py
@time: 2020/1/8 14:57
"""
import os
import sys
import json
# from ATM.conf.settings import BASE_DIR

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
# print(BASE_DIR)

def set_acount():
    acc_dic = {
        'id':'1234',
        'password':'abcd',
        'credit':15000,
        'balance':15000,
        'enroll_date':'2020-01-08',
        'expire_date':'2021-01-08',
        'pay_day':22,
        'acc_status':0 # 0 = normal, 1 = locked, 2 = disabled
    }
    file_path = BASE_DIR+ r'\db\accounts\%s' %acc_dic['id']
    print(file_path)
    with open(file_path, 'w') as f_obj:
        json.dump(acc_dic, f_obj)


set_acount()