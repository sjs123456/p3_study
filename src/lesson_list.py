# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : sjs

# 列表生成式
"""
def f(n):
    return n**3
a1 = [f(n) for n in range(10)]
a = [x*2 for x in range(10)]
print(a, a1)
"""
# t = (1, 2)
# a, b = t
# print(a, b)

# s = (x*2 for x in range(10))
# print(s)
# print(s.__next__())

# 生成器就是一个可迭代对象（iterable）
# for i in s:
#     print(next(s))

# 生成器一共有两种生成方式
# 1. s = (x*2 for x in range(10))
# 2. yield

# 使用yield创建生成器
# def foo():
#     print('ok')
#     yield 1
#
#     print('ok1')
#     yield 2
#
#     return None
#
#
# # print(foo)
# g = foo()
#
# print(next(g))
# print(next(g))
# # print(next(g))
#
# for i in foo():
#     print(i)

# for 后接的为可迭代对象 内部有 __iter__ 方法的都是可迭代对象

# def fib(max1):
#     n, before, after = 0, 0, 1
#     while n < max1:
#         print(before)
#         before, after = after, before+after
#         n = n + 1


# def fib(max1):
#     n, before, after = 0, 0, 1
#     while n < max1:
#         yield before
#         before, after = after, before+after
#         n = n + 1
#
# # fib(10)
# g = fib(8)
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
#
#
# for i in g:
#     print(i)


# def bar():
#     print('ok')
#     yield 1
#
#     print('ok1')
#     yield 2
#
# b = bar()
# next(b)

# def bar():
#     print('ok')
#     count = yield 1
#     print(count)
#     yield 2
#
# b = bar()
# # next(b)
# print(b.send(None)) # 相当于next(b)
# print(b.send('eee'))

# 使用yield 实现伪并发
import time
def consumer(name):
    print('%s准备开始吃包子了' %name)
    while True:
        baozi = yield
        print('包子[%s]来了,被[%s]吃了' %(baozi, name))

def producer(name):
    c = consumer('A')
    c1 = consumer('B')
    next(c)
    next(c1)
    print('')
    for i in range(1,10):
        time.sleep(1)
        print('%s做了两个包子' %name)
        c.send((2*i-1))
        c1.send(2*i)

producer('alex')