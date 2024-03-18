import sqlite3
import os
class webSiteManager:
    #初始
    @staticmethod
    def init(filepath):
        filepath=filepath+"websites.db"
        #检查文件是否存在
        if not os.path.exists(filepath):
            conn = sqlite3.connect(filepath)
            conn.execute('''CREATE TABLE WEBSITES
                   (
                   ID INTEGER PRIMARY KEY,
                   NAME           TEXT    NOT NULL,
                   URL            CHAR(50)     NOT NULL,
                   TYPE        INT,
                   RULE            CHAR(50)     NOT NULL
                  );''')

            return  conn
        conn=sqlite3.connect(filepath)
        return conn
    #获取所有
    @staticmethod
    def getAllBase(conn):

        cursor = conn.cursor()
        cursor.execute("SELECT ID,NAME,URL,TYPE,RULE FROM WEBSITES")
        return cursor.fetchall()
    @staticmethod
    def getById(conn,id):
        cursor = conn.cursor()
        cursor.execute("SELECT ID,NAME,URL,TYPE,RULE FROM WEBSITES WHERE ID=?",(id,))
        return cursor.fetchone()
    @staticmethod
    def update(conn,id,name,url,type,rule):
        cursor = conn.cursor()
        cursor.execute("UPDATE WEBSITES SET NAME=?,URL=?,TYPE=?,RULE=? WHERE ID=?",(name,url,type,rule,id))
        conn.commit()
    #添加
    @staticmethod
    def add(conn,name,url,type,rule):
        cursor = conn.cursor()
        cursor.execute("INSERT INTO WEBSITES (NAME,URL,TYPE,RULE) \
              VALUES (?,?,?,?)",(name,url,type,rule))
        conn.commit()
    #删除
    @staticmethod
    def delete(conn,id):
        cursor = conn.cursor()
        cursor.execute("DELETE from WEBSITES where ID=?",(id,))
        conn.commit()
    #修改
    @staticmethod
    def update(conn,id,name,url,type,rule):
        cursor = conn.cursor()
        cursor.execute("UPDATE WEBSITES set NAME=?,URL=?,TYPE=? ,RULE=? where ID=?",(name,url,type,rule,id))
        conn.commit()
