# -*- coding: utf-8 -*-
"""
@author: yuyang
@time: 2020/10/21 18:39
"""
from common.mysql import *
import requests,random,time


class Robot():


    def task_status(self):
        """返回任务状态"""
        return Mysql().select('select ')


    def task_import(self):
        """任务导入成功"""
        url = "http://gateway.tcljx.test.internal.forwardx.com/rpm-server/tcljx/carry/receive"
        payload = {
    "customerId":68,
    "workSpaceId":6,
    "orderNo":"{}".format(random.random()),
    "orderType":10,
    "createUser":123123,
    "createUserName":"测试用户",
    "containerList":[
        {
            "containerCode":"CN9001",
            "containerType":1,
            "stationName":"装载点-001",
            "detailList":[
                {
                    "stationName":"卸料点-001",
                    "goodsId":111,
                    "goodsName":"PVC 管1",
                    "goodsBarcode":"584938201",
                    "sortNum":1,
                    "planQty":1
                },
                {
                    "stationName":"卸料点-001",
                    "goodsId":222,
                    "goodsName":"PVC 管2",
                    "goodsBarcode":"584938202",
                    "sortNum":2,
                    "planQty":1
                },
                {
                    "stationName":"卸料点-002",
                    "goodsId":111,
                    "goodsName":"PVC 管1",
                    "goodsBarcode":"584938201",
                    "sortNum":1,
                    "planQty":1
                },
                {
                    "stationName":"卸料点-002",
                    "goodsId":222,
                    "goodsName":"PVC 管2",
                    "goodsBarcode":"584938202",
                    "sortNum":2,
                    "planQty":1
                }
            ]
        }
    ]
}
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, json=payload)
        return response.json()['status']['statusCode']


    def asser_code(self,statua_code):
        """循环任务状态:创建100，搬运中150，完成200，异常300"""
        while True:
            if self.task_status() == statua_code:
                break
            else:
                time.sleep(10)
                print("继续查询")


    def arrive_early(self):
        '''提前到达'''
        url = "http://10.3.0.207:7000/api/jobs/finish"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))


    def resume_sub_task(self):
        """异常转人工：完成"""
        url = "http://rcs.forwardx.com/api/jobs/resume_sub_task"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

if __name__ == '__main__':
    a = Robot()
    print(a.task_status())

11


