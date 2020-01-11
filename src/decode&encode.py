# -*-coding:utf-8 -*-
# author: sjs
# for python3


s = "特斯拉"
s_to_gbk = s.encode("gbk")
bytes_to_gbk = str(s_to_gbk,encoding='gbk')
# unicode_to_gbk = s_to_unicode.encode("gbk")
print(s)
# print("unicode:",s_to_unicode)
print("gbk:",s_to_gbk)
print(bytes_to_gbk)