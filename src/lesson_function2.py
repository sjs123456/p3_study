# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : sjs

# 高阶函数
# def func(n):
#     return n*n
#
# def foo(a, b, func):
#     return func(a) + func(b)
#
# print(foo(1, 2, func))

# 递归函数
# 阶乘

# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# print(factorial(3))

# 斐波那契数列

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(5))

# 内置函数

# 1.filter
def fun1(n):
    if  n != 'a':
        return n

s1 = filter(fun1, ['a', 'b', 'c'])
s2 = filter(lambda x : x != 'a', ['a', 'b', 'c'] )

print(list(s1), list(s2))