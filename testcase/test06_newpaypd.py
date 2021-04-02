# -*- encoding: utf-8 -*-
"""
================================
@File    : test06_newpaypd.py
@Time    : 2021/3/31 10:56
@Author  : 测试工程师：刘坤
@Email   : 609127365@qq.com
@Software: PyCharm
================================
"""
import unittest
from common import test_ddt as ddt
from common.handle_excel import Excel
import os
from common.handle_path import DATA_DIR
from common.handle_config import conf
import requests
from common.handle_data import replace_data
from jsonpath import jsonpath
from testcase import fixture


@ddt.ddt
class test_newpaypd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """登录接口"""
        fixture.setUp_login(cls)

    file_name = os.path.join(DATA_DIR, 'liukun.xlsx')
    excel = Excel(file_name, 'newpaypd')
    case = excel.read_data()

    @ddt.data(*case)
    def test_newpay(self, item):
        """设置交易密码"""
        # 准备用例数据
        url = conf.get('url', 'url') + item['url']
        # 准备数据
        params = eval(replace_data(item['data'], test_newpaypd))
        print(params)
        # 获取请求方式
        method = item['method']
        # 获取实际结果
        response = requests.request(method=method, url=url, json=params)
        res = response.json()
        print('实际结果：{}'.format(res))


if __name__ == '__main__':
    unittest.magin()
