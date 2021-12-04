# encoding: utf-8
# @author: wujinshu
# @file: tests_create_user_tag_api.py
# @time:2021/11/14 17:38
# @desc:

import unittest
import requests
import jsonpath
from common import public_api_infos


class TestsCreateUserTagApi(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()

    def tearDown(self) -> None:
        self.session.close()

    def test_01_create_user_tag(self):
        self._testMethodName = 'VXC_YH_001'
        self._testMethodDoc = '验证调用创建标签接口能否正常创建'
        # url_params_01 = {
        #     'grant_type': 'client_credential',
        #     'appid': 'wx582e7b69c417fc83',
        #     'secret': 'ec978c0ab0fa94701b2c6e820e981fa9'
        # }
        # response = self.session.get(
        #     url='https://%s/cgi-bin/token' % self.hosts,
        #     params=url_params_01
        # )
        # response = public_api_infos.get_access_token_api(
        #     self.session, url_params_01
        # )
        # json_body = response.json()
        # token_id = jsonpath.jsonpath(json_body, '$.access_token')[0]
        token_id = public_api_infos.get_access_token(self.session)
        url_params_02 = {
            "access_token": token_id
        }
        post_data_json = {"tag": {"name": "翼支付_09"}}
        # post_data_str = json.dumps(post_data_json, ensure_ascii=False)
        # response = self.session.post(
        #     url='https://%s/cgi-bin/tags/create' % self.hosts,
        #     params=url_params_02,
        #     data=post_data_str.encode('utf-8')
        # )
        response = public_api_infos.create_user_tag_api(
            self.session, url_params_02, post_data_json
        )
        print(response.json())
        actual_result = jsonpath.jsonpath(response.json(), '$.tag.name')[0]
        self.assertEqual(actual_result, '翼支付_09')

    def test_02_create_user_tag(self):
        self._testMethodName = 'VXC_YH_002'
        self._testMethodDoc = '验证调用创建标签接口,标签名参数于已存在的标签重名能否正常处理'
        # url_params_01 = {
        #     'grant_type': 'client_credential',
        #     'appid': 'wx582e7b69c417fc83',
        #     'secret': 'ec978c0ab0fa94701b2c6e820e981fa9'
        # }
        # response = self.session.get(
        #     url='https://%s/cgi-bin/token' % self.hosts,
        #     params=url_params_01
        # )
        # response = public_api_infos.get_access_token_api(
        #     self.session, url_params_01
        # )
        # json_body = response.json()
        # token_id = jsonpath.jsonpath(json_body, '$.access_token')[0]
        token_id = public_api_infos.get_access_token(self.session)
        url_params_02 = {
            "access_token": token_id
        }
        post_data_json = {"tag": {"name": "甜橙理财_03"}}
        # post_data_str = json.dumps(post_data_json, ensure_ascii=False)
        # response = self.session.post(
        #     url='https://%s/cgi-bin/tags/create' % self.hosts,
        #     params=url_params_02,
        #     data=post_data_str.encode('utf-8')
        # )
        response = public_api_infos.create_user_tag_api(
            self.session, url_params_02, post_data_json
        )
        print(response.json())
        actual_result = jsonpath.jsonpath(response.json(), '$.errcode')[0]
        self.assertEqual(actual_result, 45157)


if __name__ == "__main__":
    unittest.main(verbosity=2)
