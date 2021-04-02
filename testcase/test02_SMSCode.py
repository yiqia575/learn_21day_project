# -*- encoding: utf-8 -*-
"""
================================
@File    : test02_SMSCode.py
@Time    : 2021/3/25 9:38
@Author  : 测试工程师：刘坤
@Email   : 609127365@qq.com
@Software: PyCharm
================================
"""
import unittest
import requests
from common.handle_path import DATA_DIR
from common import test_ddt as ddt
from common.handle_excel import Excel
import os
from common.handle_config import conf
from jsonpath import jsonpath
from common.handle_log import log

@ddt.ddt
class SmsCode(unittest.TestCase):
    file_name = os.path.join(DATA_DIR,'liukun.xlsx')
    excel = Excel(file_name,'smscode')
    case = excel.read_data()

    @ddt.data(*case)
    def test_smscode(self,item):

        #准备用例数据
        #接口地址
        url = conf.get('url','url')+item['url']
        #请求参数
        params = eval(item['data'])
        #预期结果
        expected = item['expected']
        #请求方式
        method = item['method']
        #title
        title = item['title']

        #调用接口请求
        response = requests.request(method = method,url=url,json = params)
        #实际结果
        res = response.json()
        print('实际结果：{}'.format(res))
        print('预期结果:{}'.format(expected))
        try:
            self.assertEqual(str(expected),jsonpath(res,'$.statusCode')[0])
        except AssertionError as e:
            self.excel.write_data(row=item['case_id']+1,column=7,value='失败')
            log.error('{}用例执行失败'.format(title))
            raise e
        else:
            self.excel.write_data(row=item['case_id'] + 1, column=7, value='成功')
            log.info('{}用例执行通过！！！'.format(title))



if __name__ == '__main__':
    unittest.main()