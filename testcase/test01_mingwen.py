# -*- encoding: utf-8 -*-
"""
================================
@File    : test01_mingwen.py
@Time    : 2021/3/24 16:48
@Author  : 测试工程师：刘坤
@Email   : 609127365@qq.com
@Software: PyCharm
================================
"""
import unittest
from common import test_ddt as ddt
from common.handle_excel import Excel
from common.handle_path import DATA_DIR
import requests
import os
from common.handle_log import log
from common.handle_config import conf




@ddt.ddt
class MingWEN(unittest.TestCase):
    file_name = os.path.join(DATA_DIR, 'liukun.xlsx')
    excel = Excel(file_name, 'mingwen')
    cases = excel.read_data()

    @ddt.data(*cases)
    def test01_mingwen(self, item):

        # 第一步：准备用例数据
        # 接口地址
        url1 = conf.get('url','url')
        url = url1+item['url']
        print(url)
        # 请求参数
        params = eval(item['data'])
        # 预期结果
        expected = item['expected']
        method = item['method']
        title = item['title']

        # 第二步：调用接口获取实际结果
        responts = requests.request(method=method, url=url, json=params)
        res = responts.json()
        print('实际结果：{}'.format(res))
        print('预期结果：{}'.format(expected))
        # 断言
        try:
            self.assertEqual(str(expected), res['statusCode'])
        except AssertionError as e:
            self.excel.write_data(row=item['case_id']+1,column=7,value='失败')
            log.info('{}用例执行失败'.format(title))
            raise e
        else:
            self.excel.write_data(row=item['case_id'] + 1, column=7, value='通过')
            log.info('{}用例执行成功========'.format(title))
if __name__ == '__main__':
    unittest.main()