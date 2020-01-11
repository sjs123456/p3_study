# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : sjs

# sys 是在跟解释器进行交互

import sys
#
# def post():
#     print('post')
#
# def download():
#     pass
#
# if sys.argv[1] == 'post':
#     post()
# elif sys.argv[2] == 'download':
#     download()
# else:
#     pass

import time
# print(sys.path)
# print(sys.platform)
import os

if sys.platform == 'win32':
    os.system('dir')
else:
    os.system('ls -a')