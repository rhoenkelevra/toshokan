# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Created on Tue Aug 10 11:01:26 2021

@author: user24
"""
from module.setup.connect import connect
import re
from datetime import datetime


def returnBook():
    try:
        conn = connect()
        cur = conn.cursor(buffered=True)
    
        return_status = False
        while return_status == False:
            try:
                b_id = int(input("図書IDを入力してください。　（00　終了） \n>"))
    
            except:
                print("数字で入れてください。")
                continue
    
            if b_id == 00:
                return
    
            cur.execute(
                "SELECT * FROM logs WHERE b_id = %s AND in_date IS NULL", (b_id,)
            )
    
            # 貸出のログを確認する
            row_count = cur.rowcount
            if row_count == 0:
                print("図書は貸出されていません。")
    
                continue
    
            # LOGがある場合データを表示する
            log_results = cur.fetchone()
    
            # 貸出からアンパック
            (
                l_id,
                u_id,
                b_id,
                c_id,
                out_date,
                in_limit_date,
                in_date,
                d_flag,
                memo,
            ) = log_results
    
            # 図書のデータを読み取る
            cur.execute("SELECT b_id,title from books where b_id=%s", (b_id,))
            books_results = cur.fetchone()
    
            # 利用者データ読み取る
            cur.execute("SELECT c_id,c_name from customers where c_id=%s", (c_id,))
            customer_results = cur.fetchone()
            customer_results[0]
    
            # 日付フォーマット変更
            try:
                out_date = str(out_date)
                new_date = out_date.replace("-", "/")
    
                in_limit_date = str(in_limit_date)
                in_limit_date = in_limit_date.replace("-", "/")
            except Exception as error:
                print(error)
    
            # 確認メッセージを表示する
            print("=" * 60)
            print("図書ID：".ljust(11) + str(books_results[0]))
            print("図書名：".ljust(10) + str(books_results[1]))
            print("利用者ID:".ljust(10) + str(customer_results[0]))
            print("利用者名前:".ljust(8) + str(customer_results[1]))
            print("ログID：".ljust(12) + str(l_id))
            print("貸出日：".ljust(10) + str(new_date))
            print("貸出期限：".ljust(9) + str(in_limit_date))
            print("=" * 60)
    
            # 返却日の入力
            date_insert = False
            while date_insert == False:
                print("内容を確認してよろしければ")
                return_date = input("返却日を入力してください。(YYYY / MM / DD )  (00で中止します)\n>")
                if return_date == "00":
                    return
    
                # YYYY/MM/DD　確認
                date_format = re.search("\d\d\d\d[/]\d\d[/]\d\d", return_date)
                if not date_format:
                    print("入力できる日付は、数字および ”/” のみです。（例：2000/10/12）")
                    continue
    
                # datetimeに変更して確認
                try:
                    return_date = datetime.strptime(return_date, "%Y/%m/%d").date()
                except:
                    print("入力できる日付の範囲は0001/01/01～9999/12/31です。")
                    continue
    
                date_insert = True
    
            # DBデータ挿入と更新
        
            # 利用者のqtybooksをー１にする
            cur.execute(
                "update customers set qtybooks=qtybooks - 1  where c_id=%s",
                (c_id,),
            )

            # Bookのstatusをー１にする
            cur.execute(
                "update books set status=status + 1  where b_id=%s", (b_id,)
            )
            data = (return_date, l_id)
            sql = "update logs SET in_date=%s where l_id=%s"
            cur.execute(sql, data)

            conn.commit()

            # 最後の表示
            cur.execute("SELECT title FROM books WHERE b_id=%s", (b_id,))
            dt = cur.fetchone()
            print(f"図書「{dt[0]}」を返却しました。")

           
            return_status = True
            
    except Exception as error:
        print(error)
        conn.rollback()
        print("登録に失敗しました。")
          
    finally:
        cur.close()
        conn.close()


# returnBook()
