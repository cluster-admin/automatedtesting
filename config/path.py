# -*- coding: utf-8 -*-
"""
@author: yuyang
@time: 2020/7/30 22:05
"""

from common.settings import *


class ExcelConfig():

    testDataPant =  os.path.dirname(os.path.dirname(__file__)) +'/data/testdata.xlsx'

    testResuitPath =  os.path.dirname(os.path.dirname(__file__)) +'/data/testresult.xlsx'

    headers = {"Content-Type":"application/json","X-Lemonban-Media-Type":"lemonban.v2"}

