# -*- encoding: utf-8 -*-
"""
================================
@File    : handle_data.py
@Time    : 2021/3/26 14:20
@Author  : 测试工程师：刘坤
@Email   : 609127365@qq.com
@Software: PyCharm
================================
"""
from common.handle_config import conf
import re



def replace_data(data, cls):
    """替换用例参数"""
    while re.search("#(.+?)#", data):
        item = re.search("#(.+?)#", data)
        # 需要替换的数据
        rep_data = item.group()
        # 要替换的属性
        key = item.group(1)
        try:
            value = conf.get("test_data", key)
        except:
            value = getattr(cls, key)
        data = data.replace(rep_data, str(value))
    return data