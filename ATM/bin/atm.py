# !/usr/bin/env python
# encoding: utf-8

"""
@version: 
@author: sjs
@contact: ahusjs@163.com
@file: atm.py.py
@time: 2020/1/8 14:23
"""

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(BASE_DIR)
sys.path.append(BASE_DIR)

from ATM.core.main import run

run()