# !/usr/bin/env python
# encoding: utf-8

"""
@version: 
@author: sjs
@contact: ahusjs@163.com
@file: module_shelve.py
@time: 2020/1/8 13:57
"""

import shelve

f = shelve.open(r'SHELVE_text')

# f['info'] = {'name':'alex', 'age':'18'}

data = f.get('info')
print(data)