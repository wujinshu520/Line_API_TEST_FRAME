# encoding: utf-8
# @author: wujinshu
# @file: run_all_cases.py
# @time:2021/11/14 11:47
# @desc:
import unittest
import os
from common import HTMLTestReportCN
from common.log_utils import logger
from common.email_utlis import EmailUtlis


current_path = os.path.dirname(__file__)
case_path = os.path.join(current_path, 'testcasessss')
html_reports_path = os.path.join(current_path, 'html_reports/')

logger.info('*******接口测试开始执行*********')
discover_cases = None
try:
    discover_cases = unittest.defaultTestLoader.discover(
        start_dir=case_path,
        pattern='test*.py')
except ImportError as e:
    logger.error('测试用例路径配置出错，导致不能加载测试用例')
except Exception as e:
    logger.error('系统错误，错误原因：%s'%e.__str__())

api_case_suite = unittest.TestSuite()

if discover_cases:
    api_case_suite.addTest(discover_cases)
    logger.info('加载测试用例到测试套件成功')
else:
    logger.error('加载测试用例到测试套件失败')

# 创建测试报告路径的对象
html_reports_path_obj = HTMLTestReportCN.ReportDirectory(html_reports_path)
# 创建测试报告路径
html_reports_path_obj.create_dir('WX_API_TEST_')
# 创建测试报告网页文件的路径
html_report_flie_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
html_report_file_obj = open(html_report_flie_path, 'wb')
logger.info('创建测试报告路径：%s' % html_report_flie_path)
runner = HTMLTestReportCN.HTMLTestRunner(
    stream=html_report_file_obj,
    tester='wujinshu',
    title='微信公众平台接口测试项目',
    description='实战使用'
)
runner.run(api_case_suite)

email_body = '''
    <h1 align="center"> 接口自动化测试报告</h1>
    <P align="center">详情见附件  备注：封装后的</p>
    '''
EmailUtlis(email_body, html_report_flie_path).send_mail()
