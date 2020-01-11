# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : sjs


# 正则表达式: 匹配字符串的

# print(chr(65))

# s = 'hello world'

# print(s.find('llo'))
# ret = s.replace('ll', 'xx')
# print(ret)
# print(s.split('w'))

# 引入正则：模糊匹配

import re

s = 'hello world'
ret = re.findall('w\w{2}', s)
print(ret)

# 元字符
# . ==> 通配符代指所有字符,除了换行符
ret = re.findall('w..', s)
print(ret) #['wor']
ret = re.findall('w.l', 'hello w\nld')
print(ret) #[]

# ^ ==> 仅在字符串开始时进行匹配
ret = re.findall('h...o', s)
print(ret) #['hello']
ret = re.findall('^h...o', 'ahello world')
print(ret) #[]

# $ ==> 从结尾开始匹配
ret = re.findall('a..s$', 'addasdadds')
print(ret) #['adds']
ret = re.findall('a..s$', 'addasdaddsa')
print(ret) # []

# * ==> 重复匹配 匹配单个字符一，范围（0，+∞）
ret = re.findall('alex*', 'lasjfalexlialexxaleli')
print(ret) # ['alex', 'alexx', 'ale']

# + ==> 重复匹配 匹配单个字符一，范围（1，+∞）
ret = re.findall('ab+', 'asdhajhjabb')
print(ret) #['abb']
ret = re.findall('ab+', 'asdhajhjaasd')
print(ret) #[]
ret = re.findall('a+b', 'aaaabsdhajhjaasd')
print(ret) #['aaaab']

# ? ==> 匹配[0,1] 个字符
ret = re.findall('a?b', 'asdhajhjabb')  # 匹配0到1个a
print(ret) #['ab']

# {} ==> 匹配固定次数的指定字符
ret = re.findall('ab{2}', 'asdhajhjabb')
print(ret) #['abb']
ret = re.findall('ab{1,3}', 'absdhajhjaaabb') # 1到三个b
print(ret) #['ab','abb']

# [] ==> 字符集 (or)
ret = re.findall('a[c,d]x', 'acx')
print(ret) # ['acx']
ret = re.findall('[a-z]', 'acx')
print(ret) # ['a', 'c', 'x']
# 特殊功能：取消元字符的特殊功能(\ ^ - 例外)
ret = re.findall('[a,*]', 'acx*')
print(ret) # ['a', '*']
ret = re.findall('[1-9, a-z, A-Z]', '12ASty')
print(ret) #['1', '2', 'A', 'S', 't', 'y']

# ^ ==> 放在[] 里意味着取反
ret = re.findall('[^iu]', 'adsjakiudjs')
print(ret) # ['a', 'd', 's', 'j', 'a', 'k', 'd', 'j', 's']
ret = re.findall('[^4,5]', 'ads4,5jakiudjs')  # ^4,5 <==> ^(4,5)
print(ret) # ['a', 'd', 's', 'j', 'a', 'k', 'i', 'u', 'd', 'j', 's']

# \ ==> 后接元字符去除特殊功能，接普通字符实现特殊功能
# \d <==> [0-9] 匹配任何十进制数
# \D <==> [^0-9] 匹配任何非十进制数

# \s <==> [ \t\n\r\f\v] 匹配任何空白字符
# \S <==> [^ \t\n\r\f\v] 匹配任何非空白字符

# \w <==> [a-z0-9A-Z] 匹配任何字母数字字符
# \W <==> [^a-z0-9A-Z] 匹配任何非字母数字字符

# \b <==> 匹配一个特殊边界，也就指单词和特殊字符之间的位置
print(re.findall(r'I\b', 'hello I am a LI$T'))  #['I','I']
print(re.findall(r'\bI', 'hello I am a LI$T'))  #['I']

##########################################
# search ==> 匹配出满足条件的第一个结果
ret = re.search('ab', 'asjkdhjkhabaskdkab')
print(ret.group())  # 获取对象的值

ret = re.search('a.', 'aqj').group()
print(ret) #aq
ret = re.search('a\.', 'a.qj').group()
print(ret) #a.

print(re.findall('\\\\c', 'adhfD\c'))
print(re.search(r'\bblow', 'blowasad').group()) #blow

# () ==> 分组
print(re.search('(as)+', 'adshkajhasas').group())  # asas
ret = re.search('(?P<id>\d{3})/(?P<name>\w{3})', "wewerw123/ooo")
print(ret.group())
print(ret.group('id'))
print(ret.group('name'))

# 正则表达式的方法
# 1. findall() : 所有结果都返回到一个列表里
# 2. search() : 返回匹配到的第一个对象（object），对象可以调用group() 返回结果
# 3. match() : 只在字符串开始进行匹配，返回匹配到的第一个对象（object），对象可以调用group() 返回结果
# 4. split() : 分割
# ret = re.split('k', 'ashdkjkdk')
# print(ret)
# ret = re.split('[k,s]', 'adkisal')  # 先分前面的，再对分开的进行再分
# print(ret)
# 5. sub() 替换指定的内容
ret = re.sub('a..x', 's..b', 'asdkaalexjsahkj')
print(ret)
# 6. compile() 先编译成一个对象，再进行操作
p = re.compile('\.com')
print(p.findall('klajdlas.com/asjdkl'))