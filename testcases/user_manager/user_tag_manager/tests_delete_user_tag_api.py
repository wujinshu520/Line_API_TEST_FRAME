# encoding: utf-8
# @author: wujinshu
# @file: tests_delete_user_tag_api.py
# @time:2021/11/17 20:58
# @desc:

import unittest

import jsonpath
import requests
from common import public_api_infos


class TestsDeleteUserTagApi(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()

    def tearDown(self) -> None:
        self.session.close()

    def test_01_tagid_0(self):
        self._testMethodName = "VXC_YH_003"
        self._testMethodDoc = "验证不能删除标签ID为0的标签"
        # url_params = {
        #     'grant_type': 'client_credential',
        #     'appid': 'wx582e7b69c417fc83',
        #     'secret': 'ec978c0ab0fa94701b2c6e820e981fa9'
        # }
        # response = public_api_infos.get_access_token_api(
        #     self.session,
        #     url_params
        # )
        # json_body = response.json()
        # token_id = jsonpath.jsonpath(json_body, '$.access_token')[0]
        token_id = public_api_infos.get_access_token(self.session)
        url_params = {
            "access_token": token_id
        }
        post_data_json = {"tag": {"id": 0}}
        response = public_api_infos.delete_user_tag_api(
            self.session, url_params, post_data_json
        )

        actual_result = jsonpath.jsonpath(response.json(), '$.errcode')[0]
        self.assertEqual(actual_result, 45058, 'VXC_YH_003用例执行失败')


if __name__ == "__main__":
    unittest.main(verbosity=2)
