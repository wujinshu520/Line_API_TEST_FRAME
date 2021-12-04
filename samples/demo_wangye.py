# encoding: utf-8
# @author: wujinshu
# @file: demo_wangye.py
# @time:2021/11/27 15:35
# @desc:

"""
2px;">4.+?</div>

"""
import re
import requests

header_info = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Type': 'text/plain; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'
}
response = requests.get(
    url='https://www.baidu.com/s?wd=云班课',
    headers=header_info
)
print(response.text)
