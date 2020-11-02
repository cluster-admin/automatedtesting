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

from config.path import ExcelConfig


@ddt.ddt()
class UserManagement(unittest.TestCase):
    """用户管理测试"""

    testData = DoExcel(ExcelConfig.testDataPant, '用户管理')
    testResuit = DoExcel(ExcelConfig.testResuitPath, '用户管理')

    @ddt.data(*testData.all())
    def test_user(self,data):
        self.testData.updataData(data)
        r= requests.request(method=data['type'],url=data['url'],headers=ExcelConfig.headers,
                             data=data['json'])
        if 'id' in data['response'] :
            data['response']= data['response'].replace('id',str(r.json()['result']))
        try:
            self.assertEqual(str(r.json()),data['response'])
        except AssertionError as a:
            raise a
        else:
            return True




        # print(r.json())

        # self.testData.updataData(data,phoneid=True)
        # r= requests.request(method=data['type'],url=data['url'],headers=ExcelConfig.headers,
        #                      json=json.loads(data['json']))
    #     # 记录响应数据
    #     self.testResuit.updataData(data,id=r.json())
    #     try:
    #         self.assertEqual(str(r.json()),data['expect'])
    #     except AssertionError as f:
    #         #失败标fail及记录body
    #         self.testResuit.result(data, 7,'Fail')
    #         self.testResuit.result(data, 8,'请求的Body：{}\n请求的参数：{}\n响应的json{}：'
    #                                .format(r.request.body,r.request.headers,r.json()))
    #         raise f
    #     else:
    #         #数据库校验
    #         print(r.json()['code'])
    #         if r.json()['code'] == 0 :
    #             # 写入
    #             print(r.json()['data']['mobile_phone'])
    #             db = HandleDB().get_all(value=r.json()['data']['mobile_phone'])
    #             print(db)
    #         self.testResuit.result(data, 7,"Pass")
    #
    #
    # def tearDown(self):
    #     pass

if __name__ == '__main__':
    unittest.main()

