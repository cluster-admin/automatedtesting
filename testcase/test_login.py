# -*- coding: utf-8 -*-
"""
@author: yuyang
@time: 2020/7/30 22:21
"""

import unittest,requests,json,ddt,re,jsonpath
from common.do_excel import DoExcel
from common.mysql import HandleDB
from config.excel_config import ExcelConfig
from config.settings import *

@ddt.ddt()
class Testlogin(unittest.TestCase):

    testData = DoExcel(ExcelConfig.testDataPant, 'Sheet1')
    testResuit = DoExcel(ExcelConfig.testResuitPath, 'Sheet1')


    def setUp(self):

        pass



    @ddt.data(*testData.all())
    def test_login(self,data):
        # 更新测试数据的手机号进行请求
        self.testData.updataData(data,phoneid=True)
        # 使用更新后的测试数据进行请求
        r = requests.request(method=data['type'],url=data['url'],headers=ExcelConfig.headers,json=json.loads(data['json']))
        # 提取响应的id进行替换，写入新的excel
        self.testResuit.updataData(data,id=r.json())

        try:
            # 断言响应和更新动态json
            # self.assertEqual(str(r.json()),data['expect'])
            pass
        except AssertionError as f:
            self.testResuit.result(data, 7,'Fail')
            self.testResuit.result(data, 8,'请求的Body：{}\n请求的参数：{}\n响应的json{}：'.format(r.request.body,r.request.headers,r.json()))
            raise f
        else:
            print(r.json()['code'])
            if r.json()['code'] == 0 :
                # 写入
                print(r.json()['data']['mobile_phone'])
                db = HandleDB().get_all(value=r.json()['data']['mobile_phone'])
                print(db)

            self.testResuit.result(data, 7,"Pass")
            self.testResuit.result(data, 8, "")




    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main(verbosity=2)


