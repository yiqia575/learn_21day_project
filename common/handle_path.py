# -*- encoding: utf-8 -*-
"""
================================
@File    : handle_path.py
@Time    : 2021/3/23 16:44
@Author  : 测试工程师：刘坤
@Email   : 609127365@qq.com
@Software: PyCharm
================================
"""
import os

# 项目的根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#测试用例的目录路径
CASE_DIR = os.path.join(BASE_DIR,'testcase')

#测试报告的目录路径
REPORT_DIR = os.path.join(BASE_DIR,'report')

#日志目录的绝对路径
LOG_DIR = os.path.join(BASE_DIR,'logs')
#用例数据的项目路径
DATA_DIR = os.path.join(BASE_DIR,'data')
#配置文件目录的路径
CONF_DIR = os.path.join(BASE_DIR,'conf')