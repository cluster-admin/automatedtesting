import pymysql
from common.settings import configData

data = configData()['mysql']

class Mysql():
    '''数据库操作'''

    def __init__(self,databaseName='test_tcljx_rpm'):
        self.db = pymysql.connect(host= data['host'],
                                 user = data['user'],
                                 password = data['password'],
                                 port = data['port'],
                                 charset = data['charset'],
                                 database= databaseName)
        self.c = self.db.cursor()


    def select(self,sql,fetch=True):
        '''
        :param sql: 执行语句
        :param fetch: 返回one/all
        :return:
        '''
        try:
            self.c.execute(sql)
        except:
            self.db.rollback()
        else:
            if fetch == True:
                return self.c.fetchone()[0]
            else:
                return self.c.fetchall()[0]
        finally:
            self.db.close()
            self.c.close()

    def delect(self):
        print()

if __name__ == '__main__':

    print(True is None)



