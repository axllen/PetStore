import pymysql


class BaseDao:
    def __init__(self):
        self.connect = pymysql.connect(host='localhost',
                                       port=3306,
                                       user='root',
                                       password='123456',
                                       database='petstore',
                                       charset='utf8')
