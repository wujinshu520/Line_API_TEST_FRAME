# encoding: utf-8
# @author: wujinshu
# @file: re_demo03.py
# @time:2021/11/27 12:20
# @desc: search 函数

# search 函数  全字符串查找  找到第一个就停止
import re

str1 = 'nEwDreamEaaa'
# pattern_01 = re.compile('e\w', re.IGNORECASE)
# result_01 = re.search(pattern_01, str1)
result_01 = re.search('e\w', str1, re.I)
print(result_01.group())
