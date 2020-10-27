# -*- coding: utf-8 -*-
"""
@author: yuyang
@time: 2020/7/30 22:21
"""

import unittest
import json
import requests

import ddt

from common.excel import DoExcel
from common.mysql import HandleDB
from config.path import ExcelConfig


@ddt.ddt()
class Testlogin(unittest.TestCase):
    """类"""
    testData = DoExcel(ExcelConfig.testDataPant, 'Sheet1')
    testResuit = DoExcel(ExcelConfig.testResuitPath, 'Sheet1')
    def setUp(self):
        pass

    @ddt.data(*testData.all())
    def test_login(self,data):
        """ 更新测试数据"""
        self.testData.updataData(data,phoneid=True)
        r= requests.request(method=data['type'],url=data['url'],headers=ExcelConfig.headers,
                             json=json.loads(data['json']))
        # 记录响应数据
        self.testResuit.updataData(data,id=r.json())
        try:
            self.assertEqual(str(r.json()),data['expect'])
        except AssertionError as f:
            #失败标fail及记录body
            self.testResuit.result(data, 7,'Fail')
            self.testResuit.result(data, 8,'请求的Body：{}\n请求的参数：{}\n响应的json{}：'
                                   .format(r.request.body,r.request.headers,r.json()))
            raise f
        else:
            #数据库校验
            print(r.json()['code'])
            if r.json()['code'] == 0 :
                # 写入
                print(r.json()['data']['mobile_phone'])
                db = HandleDB().get_all(value=r.json()['data']['mobile_phone'])
                print(db)
            self.testResuit.result(data, 7,"Pass")


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
