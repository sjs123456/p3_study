# !/usr/bin/env python
# encoding: utf-8

"""
@version: 
@author: sjs
@contact: ahusjs@163.com
@file: accounts.py
@time: 2020/1/8 16:12
"""
import os
import sys
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(BASE_DIR)
sys.path.append(BASE_DIR)
from ATM.conf.settings import SUPER_ACCOUNT
from ATM.core.db_handler import db_handler
from ATM.conf.settings import DATABASE
# from ATM.core.logger import logger
import base64


def lock_account(account, log_obj):
    """
    锁定账号
    :param account:
    :param log_obj:
    :return:
    """
    change_user_data(account, acc_status=1)
    log_obj.info('{0} is locked by input wrong password over 3 times'.format(account))

def unlock_account(account, super_acc, password, log_obj):
    """
    解锁账号
    :param account:
    :param log_obj:
    :return:
    """
    if SUPER_ACCOUNT.get(super_acc) == password:
        change_user_data(account, acc_status=0)
        log_obj.info( '{0} is unlocked by {1}'.format(account, super_acc))

def change_user_data(account, **kwargs):
    """
    修改用户信息并返回用户新信息
    :param account:
    :param kwargs:
    :return:
    """
    db_path = r'%s/%s' % (db_handler( DATABASE ), account)
    with open( db_path, 'r' ) as acc_f:
        account_data = json.load(acc_f)
    if kwargs != {}:
        for i in kwargs:
            account_data[i] = kwargs.get(i)
        with open( db_path, 'w' ) as acc_f:
            json.dump(account_data, acc_f)
    del account_data['password']
    return account_data







if __name__ == "__main__":
    # unlock_account('1234', 'sjs', '123456',logger('access'))
    # change_user_data(1234, acc_status = 1)
    # print(change_user_data('1234'))
    print(show_user_data('1234'))

