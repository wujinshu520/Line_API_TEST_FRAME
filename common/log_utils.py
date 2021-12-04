# encoding: utf-8
# @author: wujinshu
# @file: log_utils.py
# @time:2021/11/17 19:48
# @desc:

import os
import logging
import time

current_path = os.path.dirname(__file__)
log_output_path = os.path.join(current_path, '..', 'logs')


class LogUtils(object):
    def __init__(self, log_path=log_output_path):
        self.log_flie_path = os.path.join(
            log_path, 'api_test_log_%s.log' % time.strftime('%Y%m%d'))
        self._logger = logging.getLogger("WX_api_test_log")  # 创建日志对象
        self._logger.setLevel(10)  # 设置默认等级

        console_handeler = logging.StreamHandler()  # 控制台输出日志
        file_handler = logging.FileHandler(self.log_flie_path, 'a', encoding='utf-8')  # 文件输出日志
        # 创建来一个日志格式对象
        formatter = logging.Formatter(
            "%(asctime)s__%(name)s__%(levelname)s__%(message)s"
        )
        console_handeler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self._logger.addHandler(console_handeler)
        self._logger.addHandler(file_handler)

        console_handeler.close()
        file_handler.close()

    def get_logger(self):
        return self._logger


# 建议日志用一个对象去输出
logger = LogUtils().get_logger()

if __name__ == "__main__":
    logger = LogUtils().get_logger()
    logger.info('info!!!!')
