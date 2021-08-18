# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 11:01:26 2021

@author: user24
"""
from module.setup.connect import connect
from datetime import datetime
import re


def returnBook():

    conn = connect()
    cur = conn.cursor(buffered=True)
    return_status = False
    while return_status == False:
        try:
            b_id = int(input("図書IDを入れてください。　（00　終了） \n>"))

        except:
            print("数字で入れてください。")
            continue

        if b_id == 00:
            return

        cur.execute(
            "SELECT * FROM log WHERE b_id = %s AND in_date IS NULL", (b_id,)
        )

        # 貸出のログを確認する
        row_count = cur.rowcount
        if row_count == 0:
            print("「図書は貸出されていません。")

            continue

        # ログがある場合データを表示する
        log_results = cur.fetchall()
        for row in log_results:
            l_id, u_id, b_id, c_id, out_date, in_limit_date, in_date, d_flag, memo = row

        # 図書のデータを表示する
        cur.execute("SELECT b_id,title from books where b_id=%s", (b_id,))
        books_results = cur.fetchall()
        for row in books_results:
            print("=" * 20)
            print("図書ID：　", row[0])
            print("図書名：　", row[1])

        # 利用者データ表示する
        cur.execute(
            "SELECT c_id,c_name from customer where c_id=%s", (c_id,)
        )
        customer_results = cur.fetchone()
        customer_results[0]

        print("利用者のID: ", customer_results[0])
        print("利用者の名前: ", customer_results[1])
        try:
           
    
            print("ログID：　", l_id)
    
            out_date = str(out_date)
            new_date = out_date.replace("-", "/")
            
            in_limit_date = str(in_limit_date)
            in_limit_date = in_limit_date.replace("-", "/")
            print("貸出日：　", new_date)
            print("貸出期限：　", in_limit_date)
            print("=" * 20)
    
            # 返却日の入力
    
            date_insert = False
            while date_insert == False:
                return_date = input("返却日を記入してください。(YYYY / MM / DD )  (00で中止します。)\n>")
                if return_date == "00":
                    break
    
                date_format = re.search("\d\d\d\d[/]\d\d[/]\d\d", return_date)
                if not date_format:
                    print("入力できる日付は、数字および ”/” のみです。（例：2000/10/12）")
                    continue
                try:
                    return_date = datetime.strptime(return_date,"%Y/%m/%d").date()
                except:
                    print("入力できる日付の範囲は1/01/01～9999/12/31にしてください。")
                    continue
                
                date_insert = True
                 
                
            # 利用者のqtybooksをー１にする
            cur.execute(
                "update customer set qtybooks=qtybooks - 1  where c_id=%s", (c_id,)
            )
    
            # Bookのstatusをー１にする
            cur.execute(
                "update books set status=status - 1  where b_id=%s", (b_id,)
            )
            data = (return_date, l_id)
            sql = "update log SET in_date=%s where l_id=%s"
            cur.execute(sql, data)
            
            conn.commit()
    
            # 最後の表示
            cur.execute("SELECT title FROM books WHERE b_id=%s", (b_id,))
            dt = cur.fetchone()
            print("図書", dt[0], "を返却しました。")
            
        except:
            conn.rollback()
            print("登録に失敗しました。")
            
        return_status = True

        cur.close()
        conn.close()


returnBook()