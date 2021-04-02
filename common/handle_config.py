# -*- encoding: utf-8 -*-
"""
================================
@File    : handle_config.py
@Time    : 2021/3/24 8:58
@Author  : 测试工程师：刘坤
@Email   : 609127365@qq.com
@Software: PyCharm
================================
"""
import os
from configparser import ConfigParser
from common.handle_path import CONF_DIR


class Config(ConfigParser):
    def __init__(self, filename, encoding='utf-8'):
        super().__init__()
        self.read(filename, encoding=encoding)

    pass


# 创建一个配置文件解析器

conf = Config(os.path.join(CONF_DIR,'config.ini'))

if __name__ == '__main__':

# 读取配置文件
    res = conf.get('report', 'file_name')
    print(res,type(res))
