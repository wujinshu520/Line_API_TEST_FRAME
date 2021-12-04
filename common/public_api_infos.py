# encoding: utf-8
# @author: wujinshu
# @file: public_api_infos.py
# @time:2021/11/14 20:20
# @desc:
import json
import logging

import jsonpath
from requests.exceptions import RequestException
from common.config_utils import config
from common.log_utils import logger


def get_access_token_api(session, url_params):
    logger.info('***********************************************')
    logger.info('****** 执行调用get_access_token_api接口开始 ******')
    try:
        response = session.get(
            url='https://%s/cgi-bin/token' % config.HOSTS,
            params=url_params)
    except RequestException as e:
        logger.error('请求出现异常，错误原因是：%s'%e.__str__())
    finally:
        logger.info('****** 执行调用get_access_token_api接口结束 ******')
    return response


def get_access_token(session):
    url_params = {
        'grant_type': 'client_credential',
        'appid': config.APPID,
        'secret': config.SECRET
    }
    repsonse = get_access_token_api(session, url_params)
    token_value = jsonpath.jsonpath(repsonse.json(), '$.access_token')[0]
    return token_value


def create_user_tag_api(session, url_params, post_data_json):
    post_data_str = json.dumps(post_data_json, ensure_ascii=False)
    response = session.post(
        url='https://%s/cgi-bin/tags/create' % config.HOSTS,
        params=url_params,
        data=post_data_str.encode('utf-8')
    )
    return response


def delete_user_tag_api(session, url_params, post_data_json):
    response = session.post(
        url='https://%s/cgi-bin/tags/delete' % config.HOSTS,
        params=url_params,
        json=post_data_json
    )
    return response
