# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : sjs

import re
# s ='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'




def getElements(countStr):
    while'(' in countStr:
        ret = re.search(r'\([^()]+\)', countStr).group()
        ret1 = countchengchu(ret)
        # print(ret1)
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
        return eval(countStr)



# s1 = '9-3.3333333333333335+173134.50000000003+5680/14'
def countchengchu(countStr):
    """
    计算算式中含有乘法和除法的结果
    :param countStr:
    :return:
    """
    while ('*' in countStr) or ('/' in countStr):
        ret = re.search(r'[^-+(]+[*/][^)-+/*]+', countStr).group()
        # print('ret:', ret)
        result = str(eval(ret))
        # print('result', result)
        countStr = re.sub(r'[^-+(]+[*/][^)-+/*]+', result, countStr, count=1)
        # print('countStr', countStr)
    else:
        return str(eval(countStr))

def  runApp():
    while True:
        countStr = input('请输入您要计算的算式\n>>> :')
        countStr = re.sub(' ', '', countStr)
        print(eval(countStr))
        # try:
        #     countStr = re.sub(' ', '', countStr)
        #     countResult = getElements(countStr)
        #     print('计算结果为%s' %countResult)
        # except Exception as e:
        #     print(e)

runApp()