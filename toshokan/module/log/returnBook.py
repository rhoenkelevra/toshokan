# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 11:01:26 2021

@author: user24
"""

import mysql.connector as mydb

def connect():
    conn = mydb.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    password = "pass",
    database = "toshokan"
) 
    return conn



def returnBook():
    con = connect()
    cursor = con.cursor()
    
    condition = True

    while condition == True:
        
        b_id = int(input("BookIDを入れてください。　（00　終了） \n>"))\
            
        if b_id == 0:
            break
    
        cursor.execute(
        "SELECT * FROM log WHERE b_id = %s AND in_date IS NULL",
        (b_id,))
        
        # 貸出のログを確認する
        row_count = cursor.rowcount
        if row_count == 0:
            print("「図書は貸出されていません。")
            continue
    
        # ログがある場合データをプリント
        log_results = cursor.fetchall()
        
        for row in log_results:
            l_id, u_id, b_id, c_id, out_date, in_date, d_flag, memo = row
            
        # 図書のデータ
        cursor.execute("SELECT b_id,title from books where b_id=%s", (b_id,) )
        books_results = cursor.fetchall()
        for row in books_results:
            print("=" * 20)
            print("図書ID：　", row[0])
            print("図書タイトル：　", row[1])
            
        # 利用者データ
        cursor.execute("SELECT c_id,c_name from customer where c_id=%s", (c_id,) )
        customer_results = cursor.fetchall()
        
        for row in customer_results:
            print("利用者のID: ", row[0])
            print("利用者の名前: ", row[1])
            
        # 利用者のqtybooksをー１
        cursor.execute("update customer set d-flag =　d_flag -1  where c_id=%s", (c_id,) )
        customer_results = cursor.fetchall()   
       
            
        print("ログID：　", l_id)
        print("貸出日：　", out_date)
        print("=" * 20)
            
       
        
        # l_id = int(input("Logを入れてください。　（ｑ　終了） \n>"))\
             
       
            
        # return_date = input("返却日を記入してください。(YYYY / MM / DD )\n>")
        
      
        # data = (return_date, l_id)
        # sql = "update log SET in_date=%s where l_id=%s"
        # cursor.execute(sql, data)
        con.commit()
        # print("図書～を返却しました。")
        # condition = False
    
    
returnBook()
    

    


