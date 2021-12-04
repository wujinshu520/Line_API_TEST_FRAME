# encoding: utf-8
# @author: wujinshu
# @file: re_demo05.py
# @time:2021/11/27 13:07
# @desc:

# re.split()

import re

str1 = '中国$韩国$泰国$英国'
print(str1.split('$'))

str2 = '中国1韩国2泰国3英国'
# maxsplit  maxsplit=1 分隔一次，默认为0，不限制
print(re.split('\d', str2, maxsplit=2))

str3 = '中国 韩国  泰国        英国   德国'
print(re.split('\s+', str3))
