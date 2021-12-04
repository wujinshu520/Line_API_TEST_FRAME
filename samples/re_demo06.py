# encoding: utf-8
# @author: wujinshu
# @file: re_demo06.py
# @time:2021/11/27 13:14
# @desc:

import re

str1 = '135   7766   8899  ,湖南号码'
str1 = str1.replace(' ', '')
print(str1)

result_01 = re.sub('\d\s+\d', '', str1)
print(result_01)

result_02 = re.sub('(\d\s+\d)', '', str1)
print(result_02)

result_03 = re.sub('(\d+) (\d+) (\d+)', r'1\2\3', str1)
print(result_03)
