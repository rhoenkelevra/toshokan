# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 09:08:44 2021

@author: user24
"""
import mysql.connector as mydb


def connect():
    conn = mydb.connect(
        host="localhost", port="3306", user="root", password="pass", database="toshokan"
    )
    return conn


def log():
    con = connect()
    cur = con.cursor()

    user_id = input("自分のユーザIDを記入してください。 \n>")
    book_id = input("図書のIDを入力してしてください。　\n>")
    customer_id = input("カスタマーIDを入力してください。　\n>")
    out_date = input("図書を借りた日付を記入してください。　\n>")
    memo = input("備考がある場合記入してくださいください。　\n>")

    data = (user_id, book_id, customer_id, out_date, memo)

    cur.execute(
        "insert into log (u_id, b_id, c_id, out_date, memo) values(%s, %s, %s, %s, %s)",
        data,
    )

    con.commit()
    print("登録しました。")
    cur.close()
    con.close()


log()
