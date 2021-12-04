# encoding: utf-8
# @author: wujinshu
# @file: config_utils.py
# @time:2021/11/14 19:21
# @desc:
'''
# 方式一：
class ConfigUtils(object):
    @property   # 方法 == 变成属性方法
    def HOSTS(self):
        return 'api.weixin.qq.com'
config = ConfigUtils()
if __name__ == "__main__":
    print(config.HOSTS)
'''

import configparser
import os

config_file_path = os.path.join(
    os.path.dirname(__file__), '..', 'conf', 'config.ini'
)


# 方法二：
class ConfigUtils(object):
    def __init__(self, config_flie=config_file_path):
        self.cfg_obj = configparser.ConfigParser()
        self.cfg_obj.read(config_flie, encoding='UTF_8')

    @property
    def HOSTS(self):
        hosts_value = self.cfg_obj.get('default', 'HOSTS')
        return hosts_value

    @property
    def CASE_PATH(self):
        cases_path_value = self.cfg_obj.get('path', 'CASE_PATH')
        return cases_path_value

    @property
    def APPID(self):
        appid_value = self.cfg_obj.get('user_info', 'APPID')
        return appid_value

    @property
    def SECRET(self):
        secret_value = self.cfg_obj.get('user_info', 'SECRET')
        return secret_value

    @property
    def SMTP_SERVER(self):
        secret_value = self.cfg_obj.get('email', 'SMTP_SERVER')
        return secret_value

    @property
    def SENDER(self):
        secret_value = self.cfg_obj.get('email', 'SENDER')
        return secret_value

    @property
    def PASSWORD(self):
        secret_value = self.cfg_obj.get('email', 'PASSWORD')
        return secret_value

    @property
    def RECEIVER(self):
        secret_value = self.cfg_obj.get('email', 'RECEIVER')
        return secret_value

    @property
    def CC(self):
        secret_value = self.cfg_obj.get('email', 'CC')
        return secret_value

    @property
    def SUBJECT(self):
        secret_value = self.cfg_obj.get('email', 'SUBJECT')
        return secret_value


config = ConfigUtils()

if __name__ == "__main__":
    print(config.HOSTS)
    print(config.CASE_PATH)
    print(config.APPID)
    print(config.SECRET)
    print(config.SMTP_SERVER)
    print(config.SENDER)
    print(config.PASSWORD)
    print(config.RECEIVER)
    print(config.CC)
    print(config.SUBJECT)
