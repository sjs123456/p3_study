# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : sjs

# print('----function 1')
# f = open('log.txt','a')
# f.write('2020-01-02 exec function')

# def f():
#     print('ok')
#
# f()

#
# def printInfo(name, age):
#     print('Name: %s, Age : %d' % (name, age))
#
# printInfo('XiaoHu', 18)
# printInfo(age=18, name='xiaohu')
#
# # 默认参数
# def printInfo(name, age, sex='male'):
#     print('Name: %s, Age : %d, Sex : %s' % (name, age, sex))
#
# printInfo('wuchao', 40, sex='female')
# printInfo('wuhao', 18)

# 传入元祖的不定长参数
# def add(*nums):
#     sum = 0
#     for i in nums:
#         sum += i
#     print(sum)
#
# add(1,23,4,5,6)

# 传入字典形式的不定长参数
def printInfo(**kwargs):
    for i in kwargs:
        print('%s ：%s' % (i, kwargs[i]))


printInfo(name = 'XiaoHu', age = 18)