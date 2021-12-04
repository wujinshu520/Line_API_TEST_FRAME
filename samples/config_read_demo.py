# encoding: utf-8
# @author: wujinshu
# @file: config_read_demo.py
# @time:2021/11/14 19:36
# @desc:
import configparser  # 1、导入内置包
import os

config_file_path = os.path.join(
    os.path.dirname(__file__), '..', 'conf', 'config.ini'
)
print(config_file_path)

cig_obj = configparser.ConfigParser()  # 2、创建一个配置文件对象
cig_obj.read(config_file_path,encoding='UTF-8')  # 3、配置文件对象加载配置文件
value = cig_obj.get('default', 'HOSTS')  # 4、使用get方法进行取值
value = cig_obj.get('path', 'CASE_PATH')
print(value)
