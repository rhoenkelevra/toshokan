# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 10:47:10 2021

@author: user24
"""
# from module.setup.connect import connect
import mysql.connector as mydb


def connect():
    conn = mydb.connect(
        host="localhost",
        port="3306",
        user="root",
        password="pass",
        database="toshokan",
    )
    return conn


class Login:
    con = connect()
    cursor = con.cursor(buffered=True)

    def __init__(self):
        self.login = 0

    def login_user(self, u_id, u_pass):
        con = Login.con
        cursor = Login.cursor
        success = False
        data = (u_id, u_pass)
        cursor.execute("SELECT * FROM users where u_id=%s and u_pass=%s ", data)
        rows = cursor.fetchall()
        if cursor.rowcount == 1:
            print(f"ようこそ {rows[0][1]} さん。")
            for row in rows:
                print(row)
            success = True
            self.login = rows[0][0]
        else:
            print("ログインIDまたはパスワードが違います。")
        cursor.close()
        con.close()
        return success

    def logout(self):
        self.login = 0
        print("ログアウトしました。")
