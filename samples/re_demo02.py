# encoding: utf-8
# @author: wujinshu
# @file: re_demo02.py
# @time:2021/11/27 11:55
# @desc: macth 函数


import re

str1 = 'hello123hello'

str2 = '''hello123hello
hello1hello
'''
# result01 = re.match('\d+hello', str1)  # match 匹配开头
result = re.match('hello[\d,\D]+h', str2)
# print(result.group())

str3 = '''newdream come on!
newdream come good
'''
result02 = re.match('(.+) (.+) (.+)!', str3)
print(result02.group())
print(result02.group(3))
print(result02.group(1))
print(result02.group(1, 3))

result03 = re.match('(.+) COme (.+)!\s', str3, re.I)
print(result03)
