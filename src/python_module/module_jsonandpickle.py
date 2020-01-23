# !/usr/bin/env python
# encoding: utf-8

"""
@version: 
@author: sjs
@contact: ahusjs@163.com
@file: module_jsonandpickle.py
@time: 2020/1/8 11:22
"""

import json

dic = {'name':'alex', 'age':'18'}
f = open('JSON_text', 'w')
data = json.dumps(dic)
f.write(data)
f.close()


import json  # 将其他数据类型进行序列化，多种开发语言都有的
import pickle
# f = open('JSON_text', 'r')
# data = f.read()
# data = json.loads(data)
# print(data['name'])
# f.close()

# def foo():
#     print('foo...')


# pickle 将函数/类等进行序列化 python 自身提供的
# data = json.dumps(foo)
# data = pickle.dumps(foo)
# f = open('PICKLE_text', 'wb')
# f.write(data)
# f.close()
#
#
# f = open('PICKLE_text', 'rb')
# data = f.read()
# data = pickle.loads(data)
# data()

# dump

dic = {'name':'alex', 'age':'18'}
f = open('JSON_text', 'w')
json.dump(dic, f)
f.close()

# dump 和 dumps 的区别，均为从文件中获取