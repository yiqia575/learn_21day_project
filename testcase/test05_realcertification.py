# -*- encoding: utf-8 -*-
"""
================================
@File    : test05_realcertification.py
@Time    : 2021/3/25 15:35
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
from jsonpath import jsonpath
from common.handle_log import log
from common.handle_data import replace_data
@ddt.ddt
class longin(unittest.TestCase):
    file_name = os.path.join(DATA_DIR,'liukun.xlsx')
    excel = Excel(file_name,'realcertification')
    case = excel.read_data()
    @ddt.data(*case)
    def test_login(self,item):
        #准备用例数据
        params = eval(replace_data(item['data'],longin))
        print(params)
        # params = eval(item["data"])
        url = conf.get('url','url')+item['url']
        method = item['method']
        title = item['title']
        expected = item['expected']
        response = requests.request(method=method,url=url,json = params)
        res = response.json()
        print('实际结果：{}'.format(res))
        print('预期结果：{}'.format(expected))

        try:
            self.assertEqual(str(expected), jsonpath(res, '$.statusCode')[0])
        except AssertionError as e:
            log.error('{}用例执行失败'.format(item['title']))
            self.excel.write_data(row=item['case_id'] + 1, column=7, value='失败')
            raise e
        else:
            log.error('{}用例执行成功'.format(item['title']))
            self.excel.write_data(row=item['case_id'] + 1, column=7, value='成功')
        try:
            if 'token' in res['data']:
                longin.token = jsonpath(res,'$..token')[0]

        except :
            pass

if __name__ == '__main__':
    unittest.main()