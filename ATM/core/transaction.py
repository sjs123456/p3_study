# !/usr/bin/env python
# encoding: utf-8

"""
@version: 
@author: sjs
@contact: ahusjs@163.com
@file: transaction.py
@time: 2020/1/8 16:11
"""
import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
from ATM.core.auth import login_required
from .accounts import change_user_data


@login_required
def repay(acc_data, log_obj):
    """
    还款
    :param acc_data:
    :return:
    """
    balance = acc_data['account_data']['balance']
    credit = acc_data['account_data']['credit']
    if  balance >=  credit:
        print('您当前的额度为%s,余额为%s,您无需还款'%(credit, balance))
    else:
        while True:
            repay_num = input('您当前的额度为 %s,余额为 %s,您需要还款的数目为 %s\n>>> : ' %(credit, balance, credit-balance))
            try:
                if float(repay_num) <= credit - balance:
                    new_acc_data = change_user_data(acc_data['id'], balance=balance+float(repay_num))
                    acc_data['account_data'] = new_acc_data
                    log_obj.info('user %s repayed %s '%(acc_data['id'], repay_num))
                    break
                else:
                    print('超出还款上限，您需要还款的金额为%s'%(credit-balance))
            except Exception as  e:
                log_obj.error(e)

@login_required
def show_user_info(acc_data, log_obj):
    """
    展示用户信息
    :param acc_data:
    :param log_obj:
    :return:
    """
    print(change_user_data(acc_data['id']))
    log_obj.info('user %s query userInfo success'%acc_data['id'])

@login_required
def withdraw(acc_data, log_obj):
    balance = acc_data['account_data']['balance']
    print('您当前的余额为%s'%balance)
    while balance > 0:
        withdraw_num = input('请输入您要取款的数目\n>>> : ')
        try:
            if type(eval(withdraw_num)) == int and int(withdraw_num) >0:
                service_charge = int(withdraw_num) * 0.005
                total_reduce = service_charge + int(withdraw_num)
                if service_charge + int(withdraw_num) <= balance:
                    new_acc_data = change_user_data(acc_data['id'], balance=balance - total_reduce)
                    acc_data['account_data'] = new_acc_data
                    log_obj.info('user %s withdraw %s money, service_charge is %s'%(acc_data['id'], int(withdraw_num), service_charge))
                    break
                else:
                    print('您的手续费和取款金额的总数超过您的余额，请重新输入')
            elif withdraw_num == 'back':
                break
            else:
                print('您的输入有误，请输入小于当前余额的整数')
        except Exception as  e:
            log_obj.error(e)

