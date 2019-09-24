#_*_coding=utf-8_*_

import pywinauto
from pywinauto.mouse import *
from pywinauto.keyboard import *

app = pywinauto.Application().start("notepad.exe")
title_notepad = u'无标题-记事本'