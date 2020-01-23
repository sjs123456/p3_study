# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : sjs

import re
s ='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

# com = re.compile('\(\)')

# s = re.sub(' ', '', s)
# print(s)

# print(com.search(s).group())

# ret = re.findall(r'\([^()]+\)', s)
# print(ret)
countStr = re.sub(' ', '', s)

def getElements(countStr):

    while '*' in countStr or '/' in countStr:
        ret = re.search(r'\([^()]+\)', countStr).group()
        ret1 = countchengchu(ret)
        print(ret1)
        countStr = re.sub(r'\([^()]+\)', ret1, countStr, count=1)
        if '+-' in countStr:
            countStr = re.sub(r'\+\-', '-', countStr)
        elif '++' in countStr:
            countStr = re.sub( r'\+\+', '+', countStr )
        elif '-+' in countStr:
            countStr = re.sub( r'\-\+', '-', countStr )
        elif '--' in countStr:
            countStr = re.sub( r'\-\-', '-', countStr )
    else:
        return countStr



# s1 = '9-3.3333333333333335+173134.50000000003+5680/14'
def countchengchu(countStr):
    """
    计算算式中含有乘法和除法的结果
    :param countStr:
    :return:
    """
    while ('*' in countStr) or ('/' in countStr):
        ret = re.search(r'', countStr).group()
        print('ret:', ret)
        result = str(eval(ret))
        print('result', result)
        countStr = re.sub(r'[^-+]+[*/][^-+/*()]+', result, countStr, count=1)
        print('countStr', countStr)
    else:
        return str(eval(countStr))

# print(countchengchu(s1))
# print(getElements(countStr))

s2 = '9-3.3333333333333335+122222222223.321212121212121213)*2.231*568/2930193.1231231'
ret = re.search(r'\d+\.?\d*[*/]\d+\.?\d*', s2)

print(ret)
