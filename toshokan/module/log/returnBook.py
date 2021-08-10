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
        l_id = int(input("ログIDを入れてください。　（ｑ　終了） \n>"))\
            
        if l_id == 'q':
            break
    
        cursor.execute(
        "SELECT * FROM log WHERE l_id = %s GROUP BY l_id",
        (l_id,)
    )
        results = cursor.fetchall()
        for row in results:
            print(row)
       
        
        row_count = cursor.rowcount
        if row_count == 0:
            print("It Does Not Exist")
            continue
        
        ans = input("これが正しいですか。　（YかN）")
        
        if ans == 'Y':
            return_date = input("返却日を記入してください。\n>")
            
            condition = False
    
    
    
    
    data = (return_date, l_id)
    sql = "update log SET in_date=%s where l_id=%s"
    
    cursor.execute(sql, data)
    

    con.commit()
    print("変更できました。")
    
    
returnBook()
    

    


