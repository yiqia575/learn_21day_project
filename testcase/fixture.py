# -*- encoding: utf-8 -*-
"""
================================
@File    : fixture.py
@Time    : 2021/3/31 11:47
@Author  : 测试工程师：刘坤
@Email   : 609127365@qq.com
@Software: PyCharm
================================
"""
import requests
from jsonpath import jsonpath

from common.handle_config import conf


def setUp_login(cls):
    """登录接口"""
    # 获取url
    url01 = 'longin'
    url = conf.get('url', 'url') + url01
    # 获取数据
    params = {
        "phone": "17629196006",
        "passWd": "admin@123"
    }
    # 发起接口请求
    response = requests.post(url=url, json=params)
    res = response.json()
    # 提取token
    cls.token = jsonpath(res, "$..token")[0]
    print(cls.token)
