# -*- coding: utf-8 -*-
import pymysql
import os
import sys


class OperateMySQL:
    def __init__(self,IP="10.0.0.32",username="root",pwd="123456",dbname="jingyong"):
        self.cursor = None

        self.db = None

        self.IP = IP              #数据库IP

        self.username = username  #用户名

        self.pwd = pwd            #密码

        self.dbname = dbname      #数据库名称

 

    #连接数据库

    def connection(self):

        self.db = pymysql.connect(self.IP, self.username, self.pwd, self.dbname, charset='utf8')

        self.cursor = self.db.cursor()

 

    #释放连接

    def __del__(self):

        if(self.db!=None):

            self.db.close()

 

    # 执行sql语句

    def excute(self,sql):

        try:

           self.cursor.execute(sql)           

           # 提交到数据库执行

           self.db.commit()

           return 1

        except:

           # Rollback in case there is any error

           self.db.rollback()

           return 0

 

    #查询

    def select(self,sql):

        try:

           # 执行SQL语句

           self.cursor.execute(sql)

           # 获取所有记录列表

           results = self.cursor.fetchall()

           return results

        except:

           print ("Error: unable to fecth data")

            
if __name__ == "__main__":
    # read names from text, then insert into jingyong.character
    with open("person_name.txt", "r", encoding='utf-8') as fd:
        name = fd.readline().strip("\n")
        while name:
            op = OperateMySQL()
            op.connection()
            sql = "INSERT INTO jingyong.character (Names) VALUES ('%s');" % (name)
            op.excute(sql)
            name = fd.readline().strip("\n")
        

 
