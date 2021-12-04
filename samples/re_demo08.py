# encoding: utf-8
# @author: wujinshu
# @file: re_demo08.py
# @time:2021/11/27 13:59
# @desc:

"""
data-tools='{"title":"云班课 - 用户登录","url":"http://www.baidu.com/link?
data-tools='{"title":"云班课 - 智能教学助手","url":"http://www.baidu.com/link?

"title":".+?","url"

opr-toplist1-subtitle_3FULy">+(.+?)\s+[\s\S]+?([4-9][0-9][0-9]万?)</div>



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
body_str = response.text
titls = re.findall('"title":"(.+?)","url"', body_str)
print(titls)

contents = re.findall('opr-toplist1-subtitle_3FULy">(.+?)\s+[\s\S]+?([4-9][0-9][0-9]万?)</div>', body_str)
print(contents)
