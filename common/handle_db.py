# -*- encoding: utf-8 -*-
"""
================================
@File    : handle_db.py
@Time    : 2021/3/25 16:47
@Author  : 测试工程师：刘坤
@Email   : 609127365@qq.com
@Software: PyCharm
================================
"""
import pymysql

from common.handle_config import conf


class DB:
    """连接数据库"""

    def __init__(self, host, port, password, user):
        self.con = pymysql.connect(host=host,
                                   port=port,
                                   user=user,
                                   password=password,
                                   charset="utf8",
                                   cursorclass=pymysql.cursors.DictCursor,

                                   )
        # 第二步：创建一个游标对象
        self.cur = self.con.cursor()

    def find_data(self, sql):
        """查询数据"""
        # 先提交事务，同步数据库最新的数据状态，然后再去查询
        self.con.commit()
        self.cur.execute(sql)
        res = self.cur.fetchall()
        return res


db = DB(host=conf.get("mysql", "host"),
        port=conf.getint("mysql", "port"),
        user=conf.get("mysql", "user"),
        password=conf.get("mysql", "password")
        )
if __name__ == '__main__':
    sql = 'SELECT * FROM interface_one.user_login WHERE PHONE = 17716550833;'
    res =db.find_data(sql)
    print(res,type(res))
