# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : sjs


# 装饰器
import time
from functools import reduce
# def show_time(func):
#     def inner():
#         start = time.time()
#         func()
#         print(time.time() - start)
#     return inner
#
# @show_time  # foo = show_time(foo)
# def foo():
#     print('foo...')
#     time.sleep(2)
#
# foo()

# 功能函数加参数
# def show_time(func):
#     def inner(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         print(time.time() - start)
#     return inner
#
# @show_time  # foo = show_time(foo)
# def add(a, b):
#     print(a + b)
#     time.sleep(2)
#
# @show_time
# def add2(*args, **kwargs):
#     sums = reduce(lambda x, y : x + y, args)
#     print(sums)
#     time.sleep(1)
#
# add(1, 2)
# add2(1, 2, 3, 4, 5)

# 装饰器函数加参数
# def logger(flag = True):
#     def show_time(func):
#         def inner(*args, **kwargs):
#             start = time.time()
#             func(*args, **kwargs)
#             print(time.time() - start)
#             if flag:
#                 print('log...')
#         return inner
#     return show_time
#
# @logger()
# def add(*args, **kwargs):
#     print(reduce(lambda x, y: x+y, args))
#     time.sleep(1)
#
# @logger(flag=False)
# def add1(*args, **kwargs):
#     print(reduce(lambda x, y: x+y, args))
#     time.sleep(1)
#
# add(1, 23, 4, 5, 6)
# add1(1, 2, 3, 4, 5)

# user, passwd = 'alex', '123456'
# isLogin = True
# def