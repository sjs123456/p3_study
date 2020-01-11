# !/usr/bin/env python
# -*- coding:utf-8 -*-

# s = set('alex li')
# print(s)
#
# s1 = ['alvin', 'alvin', 'ee']
# s1 = set(s1)
# print(s1, type(s))
#
# # set 属性1：可hash的,无序的，元素不重复，本身是不可hash的
# li = [2, 3, 'alex']
# s = set(li)
# print(s)

# set 的取值：循环，迭代器

# 不可变集合

# s1 = frozenset(li)
# print(s1, type(s1))

# s.add('shit')
# print(s)

# s.update([1, 2, 3, 4, " ", 6, 7, 8, 9, 0, 1.23])
# s.pop()
# print(s)
# s.clear()
# print(s)
# del s
# print(s)

# set 的运算符

# print(set('alex') == set('alexexex')) # True
#
# print(set('alex') < set('alexww')) # False
#
# print(set('alex') < set('alex')) # False
#
# print(set('alex') or set('alexw'))  # 交集
#
# print(set('alext') or set('alexw'))  # 交集 =》短路了
#
# print(set('alex') and set('alexw')) # 并集

a = set('12345')
b = set('45678')

# 取交集
print(a.intersection(b))
print(a & b)

# 取并集
print(a.union(b))
print(a | b)

# 差集
print(a.difference(b))  # in a but not in b
print(a - b)

print(b.difference(a)) # in b but not in a
print(b - a)

# 对称差集
print(a.symmetric_difference(b))
print(a ^ b)
