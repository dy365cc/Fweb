# -*- coding:utf-8 -*-
__author__ = 'dodo'

import pymysql


class MyDb():

    def __init__(self):
        self.host = 'localhost'
        self.port = ''
        self.dbname = 'myflask'
        self.dbusername = 'dodo'
        self.pwd = '123456'
        self.conn = pymysql.connect(host=self.host,
                             user=self.dbusername,
                             password=self.pwd,
                             db=self.dbname,
                             cursorclass=pymysql.cursors.DictCursor)
        self.rst = []

    def __del__(self):
        self.conn.close()

    def execsql(self,sqlstr):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sqlstr)
            self.conn.commit()
        except:
            self.conn.rollback()
        '''
        finally:
            self.conn.close()
        '''
    def getdata(self,sqlstr):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sqlstr)
            self.rst = cursor.fetchall()
        except:
            self.conn.rollback()
        '''
        finally:
            self.conn.close()
        '''
if __name__ == '__main__':
    mytestdb = MyDb()
    #mytestdb.execsql("insert into  myflask.test1 values(6,'haha',13);")
    #mytestdb.execsql("delete from myflask.test1 where  age < 30")
    mytestdb.getdata("select password from user where username = 'dodo';")
    print(mytestdb.rst)