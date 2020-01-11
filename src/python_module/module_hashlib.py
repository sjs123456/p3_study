# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : sjs


import hashlib

# MD5
# m = hashlib.md5()
# print(m)
#
# m.update("hello world".encode('utf8')) # 加密数据
#
# print(m.hexdigest())
#
# m.update('alex'.encode('utf8'))
#
# print(m.hexdigest())

# sha 
m = hashlib.sha256()

m.update('hello world'.encode('utf8'))

print(m.hexdigest())