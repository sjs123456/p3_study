# !/usr/bin/env python
# encoding: utf-8

"""
@version: 
@author: sjs
@contact: ahusjs@163.com
@file: module_xml.py
@time: 2020/1/13 16:26
"""

import xml.etree.ElementTree as ET

tree = ET.parse('xml_test')
root = tree.getroot()
print(root.tag)

# 操作XML数据
for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print(i.tag, i.text)

# 修改XML数据
for node in root.iter('rank'):
    new_rank = int(node.text) + 1
    node.text = str(new_rank)
    node.set('updated', 'yes')

tree.write('xml_txt')

# 删除XML数据