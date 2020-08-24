# -*- coding: utf-8 -*-
"""
@author: yuyang
@time: 2020/8/12 16:03
"""


# -*- coding: utf-8 -*-
"""
@author: yuyang
@time: 2020/7/30 18:57
"""
import jsonpath,openpyxl
from config.settings import *
from config.excel_config import ExcelConfig



class DoExcel():


    def __init__(self,file):
        self.file = file
        self.l = openpyxl.load_workbook(self.file)
        self.s = self.l.worksheets[0]

    # def __init__(self, filename, sheet_name):
    #     self.filename = filename
    #     self.sheet_name = sheet_name

    def open(self):
        """打开工作薄，选择表单"""
        self.workbook = openpyxl.load_workbook(self.file)
        self.sheet = self.workbook['Sheet1']

    def close(self):
        """关闭工作薄对象，释放内存"""
        self.workbook.close()

    def read_data(self):
        """ :return: 列表嵌套字典的格式"""
        self.open()
        # 按行获取所有的格子
        rows = list(self.sheet.rows)
        # 获取表头行数据
        title = []
        for r in rows[0]:
            title.append(r.value)

        # 创建一个空列表 用来存放所有的用例数据
        cases = []
        # 遍历除了表头剩余的行
        for row in rows[1:]:
            # 创建一个空列表，用来存储该行的数据
            data = []
            # 再次遍历该行的每一个格子
            for r in row:
                # 将格子中的数据，添加到data中
                data.append(r.value)
            case = dict(zip(title, data))
            cases.append(case)
        # 关闭工作薄
        self.close()
        return cases

    def read_data_obj(self):
        """
        :return: 列表嵌套对象
        """
        self.open()
        # 按行获取所有的格子
        rows = list(self.sheet.rows)
        # 获取表头行数据
        title = []
        for r in rows[0]:
            title.append(r.value)

        # 创建一个空列表 用来存放所有的用例数据
        cases = []
        # 遍历除了表头剩余的行
        for row in rows[1:]:
            # 创建一个空列表，用来存储该行的数据
            data = []
            # 再次遍历该行的每一个格子
            for r in row:
                # 将格子中的数据，添加到data中
                data.append(r.value)
            # 将表头和数据打包转换为列表
            case = list(zip(title, data))
            # 创建一个对象用来保存该行用例数据
            case_obj = CaseData()
            # 遍历列表中该行用例数据，使用setattr设置为对象的属性和属性值
            for k, v in case:
                setattr(case_obj, k, v)
            # print(case_obj,case_obj.__dict__)
            # 将对象添加到cases这个列表中
            cases.append(case_obj)
        # 关闭工作薄
        self.close()
        # 返回cases(包含所有用例数据对象的列表)
        return cases



    def singleline(self):
        ''':return: excel 列头信息'''
        return  [i.value for i in self.s[1]]





    def updataPhoneId(self,data):
        """更新手机号"""
        p  = phoneid()
        if 'phoneid' in data['json']:
            data['json'] = data['json'].replace('phoneid', p)
        if 'phoneid' in data['expect']:
            data['expect'] = data['expect'].replace('phoneid', p)
        return data



    def writeJsonExpect(self,json,data,phone=phoneid()):
        '''
        测试后置更新动态参数写入进行aseert
        :param json:
        :param data:
        :param phoneid:
        :return:
        '''
        # {'code': 0, 'msg': 'OK', 'data': {'id': 2073566, 'reg_name': '1234567891', 'mobile_phone': '13799899837'},
        # 'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved'}
        if jsonpath.jsonpath(json, '$..id'):
            id =json['data']['id']
            data['expect'] = data['expect'].replace('expectid', str(id))
            data['expect'] = data['expect'].replace('phoneid',phone)

            # 打开工作薄
        self.open()
        # 写入数据
        self.sheet.cell(data['id']+1,6,data['expect'])
        self.sheet.cell(data['id']+1,5,data['json'])
        # 保存文件
        self.workbook.save(ExcelConfig.testResuitPath)
        # 关闭工作薄
        self.close()

    def result(self,data,new,v):
        self.open()
        # 写入数据
        self.sheet.cell(data['id']+1,new,v)
        # 保存文件
        self.workbook.save(ExcelConfig.testResuitPath)
        # 关闭工作薄
        self.close()


if __name__ == '__main__':
    pass

