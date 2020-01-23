# !/usr/bin/env python
# encoding: utf-8

"""
@version: 
@author: sjs
@contact: ahusjs@163.com
@file: object_1.py
@time: 2020/1/13 16:51
"""

# class Bar:
#     def foo(self, name, age, gender, content):
#         print(name, age, gender, content)
#
# bar = Bar()
# bar.foo('xiaoming', '10', 'M', 'eat')

# self
# 1. 一个形式参数
# 2. 对象指针（代指实例）

# class Bar:
#     def foo(self, content):
#         print(self, self.name, self.age, self.gender, content)
#
# bar = Bar()
#
# bar.name = 'alex'
# bar.age = 18
# bar.gender = 'M'
#
# bar.foo('hello')

# 构造方法（__init__）
class Bar:
    """
    构造方法
    """
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def foo(self, content):
        print(123,self.name, self.age, self.gender, content)

bar = Bar('alex', 84, 'M')  # 实例化类的时候会自动执行构造方法，构造方法相当与在创建的实例内创建了属性或者执行了某些方法
print(bar)
bar.foo('123')

