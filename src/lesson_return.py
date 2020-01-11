# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : sjs


# return 返回函数的结果
# def f()


# 函数的作用域 LEGB
"""
L : local
E : enclosing
G : global
B : built-in

"""

x = int(2.9)

g_count = 0
def outer():
    o_count = 1
    i_count = 3
    def inner():
        i_count = 2
        print(o_count)

    inner()

outer()

# count = 10
# def outer():
#     global count
#     print(count)
#     count = 5
#     print(count)
# outer()
# print(count)
#
def outer():
    count = 10
    def inner():
        # nonlocal count
        print(count)
        # count += 1
        # print(count)
    inner()
    print(count)

outer()