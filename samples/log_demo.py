# encoding: utf-8
# @author: wujinshu
# @file: log_demo.py
# @time:2021/11/16 21:18
# @desc:
import logging

'''
# 相当于输出语句，默认输出error级别，info是不能输出的
logging.info('info!!!')
logging.error('Error!!!')
'''

# 使用getLogger 获取Logger 对象
log_obj = logging.getLogger("wujinshu")
log_obj.setLevel(10)  # 默认级别
# 设置 handler 对象
handler = logging.StreamHandler()
handler.setLevel(10)  # 利用handler对象设置日志级别
# 创建来一个日志格式对象
formatter = logging.Formatter(
    "%(asctime)s__%(name)s__%(levelname)s__%(message)s"
)

# 把日志格式对象配置到handler对象
handler.setFormatter(formatter)

log_obj.addHandler(handler)  # 核心，把handler 对象设置加载到日志对象
# formatter --- hander --- log_obj
log_obj.debug('debug')
log_obj.info('info')
log_obj.warning('warning')
log_obj.error('error')
log_obj.critical('critical')
