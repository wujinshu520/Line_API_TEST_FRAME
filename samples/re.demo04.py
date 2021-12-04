# encoding: utf-8
# @author: wujinshu
# @file: re.demo04.py
# @time:2021/11/27 12:28
# @desc:
'''

findall函数：
findall在字符串中找到正则表达式匹配的所有子串，
并返回一个列表，如果没有找到匹配的，则返回空列表

'''

# findall()  查找所有
# re.finditer 查找所有，并返回迭代器  迭代器中都是match对象

import re

str1 = 'hello 123 hello'
result_01 = re.search('\w+', str1)
result_02 = re.findall('\w+', str1)

pattern_01 = re.compile('\w+')
result_03 = pattern_01.finditer(str1, pos=5, endpos=12)
print(type(result_03))
for r in result_03:
    print(r.group())