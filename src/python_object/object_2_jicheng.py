# !/usr/bin/env python
# encoding: utf-8

"""
@version: 
@author: sjs
@contact: ahusjs@163.com
@file: object_2_jicheng.py
@time: 2020/1/14 14:13
"""

# 继承
# 简单的示例
# class Father:   # 基类/父类
#     def bas(self):
#         print('bas...')
#
#     def foo(self):
#         print('foo..')
#
#     def val(self):
#         print('val...')
#
# class Son(Father): # 派生类/子类
#     def pin(self):
#         print('ping...')
#
#
# son = Son()  # 执行
# son.foo()

# 代码重写
# class Father:   # 基类/父类
#     def bas(self):
#         print('bas...')
#
#     def foo(self):
#         print('foo..')
#
#     def val(self):
#         print('val...')

# class Son(Father): # 派生类/子类
#     def pin(self):
#         print('ping...')
#
#     def bas(self):  # 重写
#         # super(Son, self).bas()  # 利用super 执行父类中的 bas 方法
#         Father.bas(self)
#         print('bs1..')
"""
son = Son()
son.pin() # 此处执行时self 形参传进去的为调用他的对象（son）
son.foo() # self 永远指执行他的对象
"""
# 实例，super()
# son = Son()
# son.pin() # 此处执行时self 形参传进去的为调用他的对象（son）
# son.bas()


# 多继承
# 1. 左侧优先，一条道走到黑
# 2、如果有同一个根，根最后执行
# class F1:
#     def bas(self):
#         print('bas1...')
#
#
# class S(Father, F1):
#     def cal(self):
#         print('cal...')
#
# s = S()
# s.bas()


# 多继承每执行一个最新的带self 的函数，都会重新从子类向父类重新寻找
class BaseRequest:
    def __init__(self):
        print('BaseRequest.init')

    def process_request(self):
        print("BaseRequest.process_request")

class RequestHandler(BaseRequest):
    def __init__(self):
        print('RequestHandler.init')
        # BaseRequest.__init__(self)
        super(RequestHandler, self).__init__()

    def serve_forever(self):
        print("RequestHandler.serve_forever")
        self.process_request()

    # def process_request(self):
    #     print("RequestHandler.process_request")

class Minx:
    def process_request(self):
        print("Minx.process_request")

class Son(RequestHandler, Minx):  # 多继承
    pass

son = Son()
son.serve_forever()


# 尝试读源码的执行关系
import socketserver

obj = socketserver.ThreadingTCPServer(1, 2, bind_and_activate=True)  # 创建对象
obj.serve_forever()