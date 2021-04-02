# -*- encoding: utf-8 -*-
"""
================================
@File    : run.py
@Time    : 2021/3/22 10:06
@Author  : 测试工程师：刘坤
@Email   : 609127365@qq.com
@Software: PyCharm
================================
"""
import unittest
from unittestreport import TestRunner
from common.handle_path import CASE_DIR,REPORT_DIR
from common.handle_config import conf

# 工作中用这种方法
suite = unittest.defaultTestLoader.discover(CASE_DIR)

runner = TestRunner(suite,
                    filename=conf.get('report','file_name'),
                    report_dir=REPORT_DIR,
                    title='测试报告',
                    tester='刘坤',
                    desc="金融项目测试生成的报告",
                    templates=1
                    )
runner.run()
# 发送测试报告到邮箱
runner.send_email(host="smtp.qq.com",
                  port=465,
                  user="609127365@qq.com",
                  password="algmmzptupjccbab",
                  to_addrs="609127365@qq.com")