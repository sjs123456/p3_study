# !/usr/bin/env python
# encoding: utf-8

"""
@version: 
@author: sjs
@contact: ahusjs@163.com
@file: object_memberDecrator.py
@time: 2020/1/14 17:56
"""


# 1. 成员修饰符
# 2. 特殊成员
# 3. metaclass
# 4. 异常处理
# 5. 反射
# 6. 单例模式

# 成员修饰符

# 私有字段 ==> 无法直接访问，可以间接访问
# class Foo:
#     __v = '123'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age # 字段名私有，外部无法访问
#
#     def show(self):
#         return Foo.__v
#
#
#     @staticmethod
#     def stat():
#         return Foo.__v
# obj = Foo('A', 18)
# print(obj.name)
# # print(obj.__age)
# print(obj.show())
# Foo.__V

# 2. 继承也无法获取父类里的私有字段或者方法，可以间接获取
# class F(Foo):
#
#     def __init__(self, name1):
#         super(Foo, self).__init__()
#         self.name = name1
# #
# # f1 = Foo('alex', 100)
# # print(f1.show())
#
# f = F('alex')
# print(f.show()) # 能获取到
# print(f.__v) # 不能获取

############################
# 特殊成员
# 1. __init__  类（） 自动执行
# 2. __call__ 对象() 类()() 自动执行
# 3、 __int__ int（对象）自动执行
# 4. __str__ str(对象) 自动执行
# 5.  __add__(self, other): # 两个对象相加时，自动执行第一个对象的__add__ 方法，并将第二个对象当做参数返回
# 6. __del__(self): # 析构方法啊，对象被销毁（）时，自动执行
# 7. __dict__(self):  # 将对象中所有内容通过字典的方式返回

"""
class Foo:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other): # 两个对象相加时，自动执行第一个对象的__add__ 方法，并将第二个对象当做参数返回
        return Foo('%s-%s'%(self.name, other.name), self.age + other.age)
    
    def __del__(self):
        print('析构方法')  # 对象被销毁（）时，自动执行
        
    def __dict__(self):  # 将对象中所有内容通过字典的方式返回


obj1 = Foo('alex', 18)
obj2 = Foo('eric', 19)

r = obj1 + obj2
print(r.name)
"""
#########################
# __dict__ 将对象中所有的内容通过字典的形式返回，使用方式 类/对象.__dict__
"""
class Foo:

    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Foo('alex', 18)
d = obj.__dict__  # __dict__
print(d)

ret = Foo.__dict__
print(ret)
"""
#################################################
#  __getitem__(self, item)  执行时有返回值 执行方式 obj[参数]
#  __setitem__(self, item)  执行时无返回值 执行方式 obj[key] = value
#  __delitem__(self, item)  执行时无返回值 执行方式 del obj[参数]
"""
class Foo:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getitem__(self, item):
        if type(item) == slice:
            print("qiepianchuli")
        else:
            print(''suoyingchuli")
        return item+10

    def __setitem__(self, key, value):
        print(key, value)

    def __delitem__(self, key):
        print(key)

obj = Foo('alex', 10)
print(obj[10])
obj[1] = 100
del obj[10]
obj[1:8:2]  # 切片
"""
##################################################
# __iter__
# 如果类中有__iter__方法，对象==>可迭代对象
# 对象.__iter__() 的返回值：迭代器
# for 循环，执行一个可迭代对象，对象.__iter__() 生成一个迭代器，再对这个迭代器进行next()方法

"""
class Foo:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __iter__(self):
        return iter([1,2,3,4])

# 1. 执行li 对象的类Foo 中的 __iter__ 方法， 并获取其返回值
# 2. 循环上一步中返回的对象
li = Foo('alex', 18)
for i in li:
    print(i)
"""
##########################################
# __________metaclass________
# python 中的一切事物都是对象
# 类都是“type”类的对象，对象都是以类的对象， 类()
# def function():
#     print(123)
# Foo = type('Foo', (object,), {'func':function})
#
# obj = Foo()
# obj.function()

"""
class MyType(type):

    def __init__(self,*args, **kwargs):
        print(123)

    def __call__(self, *args, **kwargs):
        self.__new__(self, *args, **kwargs)


class Foo(object, metaclass=MyType):

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        return '对象'

    def func(self):
        print('hello world')
"""

# obj = Foo()
# 执行顺序--》 解释器从上到下，先创建Foo对象（
# 1.执行Mytype中的init方法
# 2. 执行MyType中的__call__ 方法
# 3.在__call__ 方法中执行Foo对象中的__new__方法来创建Foo对象 ）
# 再创建obj 对象 执行 Foo 对象中的__init__ 方法

###############################################

# 异常处理 常见格式
"""
while True:
    try:
        inp = input('>>>:')
        print(int(inp))
    except ValueError as e:  # 出错执行
        print(e)
        print(1)
    else: # 不出错执行
        print('else')
    finally: # 最终必须执行
        pass
"""
# raise Exception() 主动抛出异常

# 自定义异常
"""
class SjsError(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message

try:
    pass
    raise SjsError('我错了。。。')
except Exception as e:
    print(e)  # 执行e对象里的__str__ 方法
"""
# assert 条件 断言，用于强制用户服从，不服从就报错，可捕获，但一般不捕获
# print(23)
# assert 1 == 2
# print(3)

##################################################

# 反射 getattr setattr hasattr
"""
class Foo:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return self.name

obj = Foo('alex', 18)
b = 'name'
print(obj.__dict__[b])

# 去什么东西里面去获取什么内容 getattr(obj, 字段)
# 通过以下函数获取或者改变对象中的元素
v = getattr(obj, 'name')
r = getattr(obj, 'show')
print(r())
print(v)

hasattr(obj, 'name')  # 判断对象中是否有该元素

setattr(obj, 'k1', 'v1')  # 在对象的内存中创建一个元素

print(getattr(obj, 'k1'))
"""

"""
from src.python_object import object_3_duotai

f = getattr(object_3_duotai, 'Foo')
print(f)

inp = input('请输入要查看的URL：')

if hasattr(object_3_duotai, inp):
    ret = getattr(object_3_duotai, inp)
    print(ret())
else:
    print('404')
"""
##############################################
# 单例模式

# 使用方式：
"""
class Foo:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.age, self.name)

obj = Foo('alex', 18)

# 单例 ==> 永远使用同一个对象（实例）
v = None
while True:
    if v:
        v.show()
    else:
        v = Foo('alex', 123)
        v.show()
"""

class Foo:

    __v = None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return cls.__v

obj1 = Foo.get_instance()
print(obj1)
obj2 = Foo.get_instance()
print(obj2)
obj3 = Foo.get_instance()
print(obj3)


