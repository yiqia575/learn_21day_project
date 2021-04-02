# -*- encoding: utf-8 -*-
"""
================================
@File    : demo04_日志收集器的封装和应用.py
@Time    : 2021/3/23 10:25
@Author  : 测试工程师：刘坤
@Email   : 609127365@qq.com
@Software: PyCharm
================================
"""
"""
需求：再执行用例的过程，记录日志，（把日志记录到文件）
        日志收集器
封装一个创建日志收集器的方法


"""
import logging
from logging.handlers import TimedRotatingFileHandler
from common.handle_path import LOG_DIR
import os
from common.handle_config import conf



def create_logger():
        """创建日志收集器"""
        #1、创建一个收集器
        log = logging.getLogger('liukun')
        log.setLevel(conf.get('logging','level')) #设置收集日志的等级
        #2、创建一个输出到文件的输出渠道(按时间轮转)
        fh = TimedRotatingFileHandler(os.path.join(LOG_DIR,'log.log'),
                                      when='d',
                                      interval=1,
                                      backupCount=7,
                                      encoding='utf-8')
        fh.setLevel(conf.get('logging','fh_level')) #设置输出等级
        log.addHandler(fh) #添加到收集器中
        #3、创建一个输出到控制台的输出渠道
        sh = logging.StreamHandler()
        sh.setLevel(conf.get('logging','sh_level')) #设置输出等级
        log.addHandler(sh) #添加到收集器中
        #设置日志输出格式
        formatter = "%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s"
        mate = logging.Formatter(formatter)
        fh.setFormatter(mate)
        sh.setFormatter(mate)


        return log
log = create_logger()

if __name__ == '__main__':
    log.debug('python666')