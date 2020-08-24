# -*- coding: utf-8 -*-
"""
@author: yuyang
@time: 2020/7/31 14:09
"""
import unittest,os,sys

from HTMLTestRunner import HTMLTestRunner
import openpyxl

import HTMLTestRunner

import time,sys


def run():
    # 生成测试报告HTML文件

    # print(a)
    dir = '../testcase'
    report_dir = '../reports'
    now = time.strftime("%Y%m%d%H%M%S")
    b = unittest.defaultTestLoader.discover(dir, pattern='test*.py')
    report_name = report_dir + '/' + now + 'Result.html'
    with open(report_name, 'wb')as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2,title='瑞幸自动化测试报告，测试结果如下：',
                                                description="运行环境 : Windows10 , Chrome 浏览器")
        # 执行测试用例文件
        runner.run(b)

if __name__ == '__main__':
    run()

# C:\Users\yuyang\AppData\Local\Programs\Python\Python38\python38.zip
# C:\Users\yuyang\AppData\Local\Programs\Python\Python38\DLLs
# C:\Users\yuyang\AppData\Local\Programs\Python\Python38\lib
# C:\Users\yuyang\AppData\Local\Programs\Python\Python38
# C:\Users\yuyang\AppData\Local\Programs\Python\Python38\lib\site-packages
#
#
# C:\Users\yuyang\PycharmProjects\automatedtesting\run
# C:\Users\yuyang\PycharmProjects\automatedtesting
#
# C:\Users\yuyang\.virtualenvs\Api
# C:\Users\yuyang\.virtualenvs\Api\lib\site-packages
# C:\Users\yuyang\.virtualenvs\Api\lib\site-packages\win32
# C:\Users\yuyang\.virtualenvs\Api\lib\site-packages\win32\lib
# C:\Users\yuyang\.virtualenvs\Api\lib\site-packages\Pythonwin