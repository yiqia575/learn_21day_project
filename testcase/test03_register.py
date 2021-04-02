# -*- encoding: utf-8 -*-
"""
================================
@File    : test03_register.py
@Time    : 2021/3/25 10:43
@Author  : 测试工程师：刘坤
@Email   : 609127365@qq.com
@Software: PyCharm
================================
"""
import unittest
import requests
from common import test_ddt as ddt
from common.handle_excel import Excel
from common.handle_path import DATA_DIR
from common.handle_config import conf
import os
from jsonpath import jsonpath
from common.handle_log import log
import random
from common.handle_db import db




@ddt.ddt
class register(unittest.TestCase):
    file_name = os.path.join(DATA_DIR, 'liukun.xlsx')
    excel = Excel(file_name, 'register')
    case = excel.read_data()
    @ddt.data(*case)
    def test_register(self, item):
        if '#smscode' in item['data']:
            item['data'] = item['data'].replace('#smscode',register.smscode)

        url = conf.get('url', 'url') + item['url']
        params = eval(item['data'])
        method = item['method']
        expected = item['expected']


        response = requests.request(method=method, url=url, json=params)
        res = response.json()
        print('实际结果：{}'.format(res))
        print('预期结果：{}'.format(expected))

        try:
            self.assertEqual(str(expected),jsonpath(res,'$.statusCode')[0])
        except AssertionError as e:
            log.error('{}用例执行失败'.format(item['title']))
            self.excel.write_data(row=item['case_id'] + 1, column=7, value='失败')
            raise e
        else:
            log.error('{}用例执行成功'.format(item['title']))
            self.excel.write_data(row=item['case_id']+1,column=7,value='成功')
        try:
            if 'smsVerificationCode' in res['data']:
                register.smscode = jsonpath(res,'$..smsVerificationCode')[0]
        except Exception:
            pass
    @staticmethod
    def random_phone():
        """随机生成一个未注册手机号"""
        while True:
            phone = '131'
            for i in range(8):
                i = random.randint(0,9)
                phone+=str(i)
            #判断手机号是否已经注册
            sql = 'SELECT * FROM interface_one.user_login WHERE PHONE = {};'.format(phone)
            res = db.find_data(sql)
            if not res:
                return phone





if __name__ == '__main__':
    res = register.random_phone()
    print(res)
