# encoding: utf-8
# @author: wujinshu
# @file: re.demo07.py
# @time:2021/11/27 13:45
# @desc:
import re

str1 = '''newdream come on!!
google come on!!'''
value = re.subn('(\w+) (\w+) (\w+)', r'\2 \3 \1', str1)
print(type(value))
print(value)