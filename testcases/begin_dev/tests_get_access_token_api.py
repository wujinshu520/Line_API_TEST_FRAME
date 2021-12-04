# encoding: utf-8
# @author: wujinshu
# @file: tests_get_access_token_api.py
# @time:2021/11/14 11:51
# @desc:
import unittest
import requests
import jsonpath
from common import public_api_infos
from common.log_utils import logger
from common.config_utils import config


class TestsGetAccessTokenApi(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()

    def tearDown(self) -> None:
        self.session.close()

    def test_01_get_access_token(self):
        ''' 【VXC_KS_001】验证获取Access_token接口是否能正常调用 '''
        logger.info('*********************************')
        logger.info('*    用例【VXC_KS_001】开始执行    *')
        try:
            url_params = {
                'grant_type': 'client_credential',
                'appid': config.APPID,
                'secret': config.SECRET
            }
            # response = self.session.get(
            #     url='https://%s/cgi-bin/token' % self.hosts,
            #     params=url_params
            # )
            response = public_api_infos.get_access_token_api(
                self.session, url_params
            )
            json_body = response.json()
            actual_result = jsonpath.jsonpath(json_body, '$.access_token')[0]
            self.assertTrue(actual_result)  # 一定要写断言语句
        except AssertionError as e:
            logger.error('用例【VXC_KS_001】断言失败')
        except Exception as e:
            logger.error('用例【VXC_KS_001】报错原因是：%s' % e.__str__())
        finally:
            logger.info('用例【VXC_KS_001】执行结束')
            logger.info('*********************************')

    def test_02_grant_type_none(self):
        self._testMethodName = 'VXC_KS_002'
        self._testMethodDoc = '验证获取Access token接口参数grant_type错误能否正常处理'
        url_params = {
            'grant_type': '',
            'appid': config.APPID,
            'secret': config.SECRET
        }
        # response = self.session.get(
        #     url='https://%s/cgi-bin/token' % self.hosts,
        #     params=url_params
        # )
        response = public_api_infos.get_access_token_api(
            self.session, url_params
        )
        json_body = response.json()
        actual_result = jsonpath.jsonpath(json_body, '$.errcode')[0]
        self.assertEqual(actual_result, 40002)  # 一定要写断言语句


if __name__ == "__main__":
    unittest.main(verbosity=2)
