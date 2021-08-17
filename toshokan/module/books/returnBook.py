# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 11:01:26 2021

@author: user24
"""
# from module.setup.connect import connect
import re
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


# con = connect()
# cursor = con.cursor(buffered=True)


def returnBook():

    con = connect()
    cursor = con.cursor(buffered=True)
    condition = True
    while condition == True:
        try:
            b_id = int(input("図書IDを入れてください。　（00　終了） \n>"))

        except:
            print("数字で入れてください。")
            continue

        if b_id == 00:
            break

        cursor.execute(
            "SELECT * FROM log WHERE b_id = %s AND in_date IS NULL", (b_id,)
        )

        # 貸出のログを確認する
        row_count = cursor.rowcount
        if row_count == 0:
            print("「図書は貸出されていません。")

            continue

        # ログがある場合データを表示する
        log_results = cursor.fetchall()
        for row in log_results:
            l_id, u_id, b_id, c_id, out_date, in_date, d_flag, memo = row

        # 図書のデータを表示する
        cursor.execute("SELECT b_id,title from books where b_id=%s", (b_id,))
        books_results = cursor.fetchall()
        for row in books_results:
            print("=" * 20)
            print("図書ID：　", row[0])
            print("図書名：　", row[1])

        # 利用者データ表示する
        cursor.execute(
            "SELECT c_id,c_name from customer where c_id=%s", (c_id,)
        )
        customer_results = cursor.fetchone()
        customer_results[0]

        print("利用者のID: ", customer_results[0])
        print("利用者の名前: ", customer_results[1])
        try:
            # 利用者のqtybooksをー１にする
            cursor.execute(
                "update customer set qtybooks=qtybooks - 1  where c_id=%s", (c_id,)
            )
    
            # Bookのstatusをー１にする
            cursor.execute(
                "update books set status=status - 1  where b_id=%s", (b_id,)
            )
    
            print("ログID：　", l_id)
    
            print(type(out_date))
            out_date = str(out_date)
            new_date = out_date.replace("-", "/")
            print("貸出日：　", new_date)
            print("=" * 20)
    
            # 返却日の入力
    
            date_insert = True
            while date_insert == True:
                print("(00で中止します。)")
                return_date = input("返却日を記入してください。(YYYY / MM / DD )\n>")
                if return_date == "00":
                    break
    
                date_format = re.search("\d\d\d\d[/]\d\d[/]\d\d", return_date)
                if not date_format:
                    print("入力できる日付は、数字および ”/” のみです。（例：2000/10/12）")
                    continue
    
                data = (return_date, l_id)
                sql = "update log SET in_date=%s where l_id=%s"
                cursor.execute(sql, data)
                date_insert = False
        except:
            con.roolback()
            
            

        con.commit()

        # 最後の表示
        cursor.execute("SELECT title FROM books WHERE b_id=%s", (b_id,))
        dt = cursor.fetchone()
        print("図書", dt[0], "を返却しました。")

        condition = False

        cursor.close()
        con.close()


# returnBook()