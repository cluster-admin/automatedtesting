# -*- coding: utf-8 -*-
"""
@author: yuyang
@time: 2020/8/2 22:58
"""
import os,time,random
"""
时间
路径
接口

"""
def gettime():
    '''日期时间'''
    print(__name__)
    return time.strftime("%Y-%m-%d %H:%M:%S")


def set_phoneid():
    ''' 生成手机号'''
    p = '1'
    p += random.choice(["0","3","5","8"])
    for i in range(9):
        p += random.choice(["0","1","2","3","4","5","6","7","8","9"])
    return p


path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path =os.path.join(path,'config')
yaml_config_path =os.path.join(config_path,'config.yaml')
testDataPant = os.path.dirname(os.path.dirname(__file__)) + '/data/testdata.xlsx'
testResuitPath = os.path.dirname(os.path.dirname(__file__)) + '/data/{}testresult.xlsx'.format(gettime())


headers = {"Content-Type": "application/json", "X-Lemonban-Media-Type": "lemonban.v2"}





