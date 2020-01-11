# import time
# times = time.strftime("%Y-%m-%d")
# def f(times):
#     print("Now time is : %s" %times)
#
# f(times)


# def show_shopping_car():
#     saving = 1000000
#     shopping_car = [
#         ('Mac', 9000),
#         ('kindle', 800),
#         ('tesla', 100000),
#         ('Python book', 105),
#     ]
#     print('您已经购买的商品如下'.center(50, '*'))
#     for i, v in enumerate(shopping_car, 1):
#         print('\033[35;1m %s:  %s \033[0m'%(i,v))
#
#     expense = 0
#     for i in shopping_car:
#         expense += i[1]
#     print( '\n\033[32;1m您的余额为 %s \033[0m' % (saving - expense) )
#
# show_shopping_car()


# def action1(n):
#     print('starting action1. . .')
#
#     with open('日志记录', 'a') as f:
#         f.write('end action %s\n' %n)
#
# def action2(n):
#     print('starting action2. . .')
#
#     with open('日志记录', 'a') as f:
#         f.write('end action %s\n' %n)
#
# def action3(n):
#     print('starting action3. . .')
#
#     with open('日志记录', 'a') as f:
#         f.write('end action %s\n' %n)
#
# action1(1)
# action2(2)
# action3(3)
# import time
#
# def logger(n):
#     time_format = '%Y-%m-%d %X'
#     time_current = time.strftime(time_format)
#     with open('日志记录', 'a') as f:
#         f.write('%s end action %s\n' %(time_current,n))
#
# def action1(n):
#     print('starting action1. . .')
#     logger(n)
#
# def action2(n):
#     print('starting action2. . .')
#     logger(n)
#
# def action3(n):
#     print('starting action3. . .')
#     logger(n)
#
# action1(1)
# action2(2)
# action3(3)


# number = [2, -5, 9, -7, 2, 5, 4, -1, 0, -3, 8]
# count = 0
# sum = 0

# for i in range( len( number ) ):
#     if number[i] > 0:
#         count += 1
#         sum += number[i]
#
# print(sum, count)
#
# if count > 0:
#     average = sum / count
#     print(average)

# from functools import reduce

# positive = filter(lambda x: x>0, number)
# # average = (reduce(lambda x, y: x+y, positive)) /
# for i in range(4):
#     print(next(positive))

# x = 6
# def f():
#     print(x)
#     x = 5
#
# f()

# def fibo(n):
#     if n <= 1:
#         return 1
#     else:
#         return (fibo(n-1) + fibo(n-2))
#
#
# print(fibo(5))
#


# 浅拷贝--仅复制数据的第一层

a = [[1, 2], 3, 4]
b = a.copy()  # shalow copy
print(b)
print(a)
b[0][0] = 2
print(b)
print(a)

husband = ['xiaohu', 123, [15000, 9000]]
wife = husband.copy()
wife[0] = 'xiaoPang'
wife[1] = 345


# 深copy
import copy

xiaosan = copy.deepcopy(husband)
xiaosan[0] = 'JinXin'
xiaosan[1] = 666
xiaosan[2][1] -= 1999

print(wife)
print(xiaosan)