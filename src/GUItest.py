#_*_coding=utf-8_*_

import pywinauto
from pywinauto.mouse import *
from pywinauto.keyboard import *
import time

#运行记事本程序
app = pywinauto.Application().start("notepad.exe")
#窗体选择
title_notepad = u'无标题-记事本'
#选择一个菜单项
# app[title_notepad].menu_select('帮助->关于记事本')
# time.sleep(3)
# #点击新弹出窗体的确定按钮
# out_note=u'关于记事本'
# button_name_ok = '确定'
# app[out_note][button_name_ok].click()
#查看一个窗体含有的控件子窗体，菜单
print(app[title_notepad].print_control_identifiers())
#在记事本中输入一些文本
# app.title_notepad.Edit.type_keys('pywinauto works!\n',with_spaces=True,with_newlines=True)
# app.title_notepad.Edit.type_keys('hello world!\n',with_spaces=True,with_newlines=True)
# app[title_notepad].menu_select('文件->保存')
#
# file_name = "test"
#
# app['另存为']['edit'].type_keys(file_name)
# app['另存为']['保存'].click()
# time.sleep(3)
# app['确认另存为']['是'].click()


