# !/usr/bin/env python
# encoding: utf-8

"""
@version: 
@author: sjs
@contact: ahusjs@163.com
@file: object_3_duotai.py
@time: 2020/1/14 16:30
"""

# ==========================================

# 小游戏
# class Human:
#     def __init__(self, name, gender, age, power):
#         self.name = name
#         self.gender = gender
#         self.age = age
#         self.power = power
#
#     def fight_in_grass(self):
#         self.power -= 200
#
#     def exercise(self):
#         self.power += 100
#
#     def fight_multi_game(self):
#         self.power -= 500
#
#
# human = Human('zhangsan', 'M', 18, 2000)
# human.fight_in_grass()
# print(human.power)

# ============================================
# 面向对象中高级

# 类成员 ==> 字段（self.name），方法(def 方法名)
# 静态字段 ==> 保存在类中

"""
class Province:
    name = 'ZG' # 静态字段， 属于类，可以通过类和对象进行访问
    country = "ZG"
    def __init__(self, name):
        self.name = name  # 普通字段 属于对象 只能通过对象访问

henan = Province('henan')
print(Province.name)
print(Province.country)
henan.name = 1
print(henan.name)
print(Province.name)
print(henan.country)
"""
# 方法 ==> 普通方法（通过对象作为中间值进行访问）
# 使用指南
# 如果对象中保存了一些值，执行某功能时，需要使用对象中的值 --》 普通方法
# 不需要任何对象中的值，静态方法

"""
class Foo:
    # 普通方法 ==> 必须建立对象才能访问
    def bar(self):
        print('bar...')

    # 静态方法 ==> 加上装饰器，使用 类直接进行访问，不需要self 参数
    @staticmethod
    def sta():
        print(123)

    # 类方法 ==> 加上装饰器，使用类直接进行访问， 需要一个参数，默认传入类名
    @classmethod
    def classmd(cls):
        # cls 是类名
        print('classmd..')
"""
"""
obj = Foo()
Foo.bar(obj)
obj.bar()

Foo.sta()

Foo.classmd()
"""

"""
class Foo:
    def __init__(self):
        self.name = 'a'

    def bar(self):
        print('bar...')

    @property  # 特性(属性) 最重要的是去除括号  按照方法的样子写，按照字段的样子调用
    def per(self):
        # print('per...')
        return 1

    @per.setter
    def per(self, val):
        print(val)

obj = Foo()
s = obj.per
print(s)
obj.per = 123
print(obj.per)
"""

class Foo:
    def f1(self):
        return 123

    per = property(fget=f1)

# obj = Foo()
# print(obj.per)

def f1():
    return 'shouye'

def f2():
    return 'caijing'

def f3():
    return 'luntan'