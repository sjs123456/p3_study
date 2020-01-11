# !/usr/bin/env python
# encoding: utf-8

"""
@version: 
@author: sjs
@contact: ahusjs@163.com
@file: main.py.py
@time: 2020/1/8 14:25
"""

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from ATM.core.logger import logger
from ATM.core.auth import acc_login
from ATM.core import transaction



acc_data = {
    'id':None,
    'isAuthed':False,
    'account_data':None
}

def interactive(acc_data, log_obj):
    menu = u'''
       ------- SJS Bank ---------
       \033[32;1m  
       1.  账户信息
       2.  还款
       3.  取款
       4.  转账
       5.  账单
       6.  退出
       \033[0m'''

    menu_dic = {
    "1": transaction.show_user_info,
    "2": transaction.repay,#( 功能已实现 )
    "3": transaction.withdraw,#( 功能已实现 )
    "4": "transfor",
    "5": "pay_bill",
    "6": "logout"
    }

    exit_flag = False
    while not exit_flag:
        print(menu)
        user_choice = input('>>>:').strip()
        if user_choice in menu_dic:
            menu_dic[user_choice](acc_data, log_obj)
        else:
            print('\033[31;1mOption does not exist!\033[0m')

def run():
    # print( 'run...' )
    new_accdata = acc_login(acc_data, logger('access'))
    interactive(new_accdata, logger('transaction'))


run()


