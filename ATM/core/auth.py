# !/usr/bin/env python
# encoding: utf-8

"""
@version: 
@author: sjs
@contact: ahusjs@163.com
@file: auth.py
@time: 2020/1/8 14:58
"""
import os
import sys
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(BASE_DIR)
sys.path.append(BASE_DIR)
# from ATM.core.logger import logger
from ATM.core.db_handler import db_handler
from ATM.conf.settings import DATABASE
from ATM.core.accounts import lock_account



def login_required(func):
    """
    检测用户是否已经登录
    :param func:
    :return:
    """
    def wrapper(*args,**kwargs):
        """
        :param args: 传入用户登录信息
        :param kwargs:
        :return:
        """
        if args[0]['isAuthed']:
            return func(*args,**kwargs)
        else:
            exit('user is not authenrized')
    return wrapper



def acc_login(acc_data, log_obj):
    """
    登录
    :param acc_data:
    :param log_obj:
    :return:
    """
    login_times_count = 0
    login_error_accont = []
    while True:
        account = input('请输入您的账号\n>>> :')
        password = input( '请输入您的密码\n>>> :' )
        login_result = acc_login_v(account, password, log_obj)
        if login_result:
            acc_data['id'] = account
            acc_data['isAuthed'] = True
            acc_data['account_data'] = login_result
            break
        else:
            login_times_count += 1
            login_error_accont.append( account )
            log_obj.info( 'user {0} login failed, failtimes:{1}'.format( account, login_error_accont.count(account) ))
            if login_error_accont.count(account) >= 3:
                lock_account(account, log_obj)
    return acc_data


def acc_login_v(account, password, log_obj):
    """
    登录验证
    :param account:
    :param password:
    :param log_obj:
    :return:
    """

    db_path = r'%s/%s' %(db_handler(DATABASE), account)
    if os.path.exists(db_path):
        with open(db_path, 'r') as acc_f:
            account_data = json.load(acc_f)
        if account_data['acc_status'] != 0:
            log_obj.info( 'user {0} login failed, account is locked '.format(account))
            return False
        else:
            if account_data['password'] == password:
                log_obj.info('user {0} login success'.format(account))
                # print(type(account_data), account_data)
                del account_data['password']
                return account_data
            else:
                log_obj.info( 'user {0} login failed, wrong password'.format(account))
                return False
    else:
        log_obj.info('user {0} login failed, no such account'.format(account))
        return False


# acc_login_v('1234', 'abcd',logger('access'))
# if __name__ == "__main__":
#     acc_login_v('1234', 'abcd',logger('access'))



