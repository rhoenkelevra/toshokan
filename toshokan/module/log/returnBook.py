# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 11:01:26 2021

@author: user24
"""

import mysql.connector as mydb
# from ..connect import connect


def connect():
    conn = mydb.connect(
        host="localhost",
        port="3306",
        user="root",
        password="rfr689022",
        database="toshokan"
    )
    return conn


def returnBook():
    con = connect()
    cursor = con.cursor(buffered=True)

    condition = True
    while condition == True:

        b_id = int(input("BookIDを入れてください。　（00　終了） \n>"))\

        if b_id == 00:
            break

        cursor.execute(
            "SELECT * FROM log WHERE b_id = %s AND in_date IS NULL", (b_id,))

        # 貸出のログを確認する
        row_count = cursor.rowcount
        print("1")
        if row_count == 0:
            print("「図書は貸出されていません。")
            continue

        # ログがある場合データを表示する
        log_results = cursor.fetchall()
        print("2")
        for row in log_results:
            l_id, u_id, b_id, c_id, out_date, in_date, d_flag, memo = row

        # 図書のデータを表示する
        cursor.execute("SELECT b_id,title from books where b_id=%s", (b_id,))
        print("3")
        books_results = cursor.fetchall()
        for row in books_results:
            print("=" * 20)
            print("図書ID：　", row[0])
            print("図書タイトル：　", row[1])

        # 利用者データ表示する
        cursor.execute(
            "SELECT c_id,c_name from customer where c_id=%s", (c_id,))
        customer_results = cursor.fetchone()
        print("4")
        customer_results[0]

        print("利用者のID: ", customer_results[0])
        print("利用者の名前: ", customer_results[1])

        # 利用者のqtybooksをー１にする
        cursor.execute(
            "update customer set qtybooks=qtybooks - 1  where c_id=%s", (c_id,))
        print(5)
        cursor.execute("select * from customer where c_id=%s", (c_id, ))
        print(6)
        customer_results = cursor.fetchall()

        print("ログID：　", l_id)
        print("貸出日：　", out_date)
        print("=" * 20)

        # 返却日の入力
        print("(00で中止します。)")
        return_date = input("返却日を記入してください。(YYYY / MM / DD )\n>")
        if return_date == '00':
            continue
        data = (return_date, l_id)
        sql = "update log SET in_date=%s where l_id=%s"
        cursor.execute(sql, data)
        con.commit()
        print(6)

        # 最後の表示
        cursor.execute("SELECT title FROM books WHERE b_id=%s", (b_id,))
        dt = cursor.fetchone()

        print(10)

        print("図書", dt[0], "を返却しました。")
        condition = False


returnBook()
