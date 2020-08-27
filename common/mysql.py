# -*- coding: utf-8 -*-
"""
@author: yuyang
@time: 2020/8/1 15:46
"""


import pymysql,yaml

from config.settings import yaml_config_path

f = open(yaml_config_path,encoding='utf-8')
data =yaml.load(f,Loader=yaml.FullLoader)


class HandleDB:

    def __init__(self):
        self.con = pymysql.connect(
            host=data['db']['host'],user=data['db']['user'],
            password=str(data['db']['password']),port=data['db']['port'],
            charset=data['db']['charset'],database=data['db']['database'])
        self.cur = self.con.cursor()

    def get_one(self, sql):
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def get_all(self, value):
        self.con.commit()
        self.cur.execute('SELECT * FROM member WHERE mobile_phone="{}"'.format(value))
        return self.cur.fetchall()

    def count(self, sql):
        self.con.commit()
        res = self.cur.execute(sql)
        return res

    def close(self):
        self.cur.close()
        self.con.close()

if __name__ == '__main__':
    pass
    a =HandleDB()
    b =a.get_all(1)
    12312312
    print(b)

