#_*_coding=utf-8_*_

import pywinauto
from subprocess import Popen
from pywinauto import Desktop
from pywinauto import mouse
from pywinauto import keyboard
import time

app = pywinauto.Application().start('D:\\Users\ex-shijs001\AppData\Local\Programs\coco_test\coco_test.exe')
main_title = 'coco_test'
app[main_title].print_control_identifiers()
# time.sleep(5)
# app.coco_test.close()
