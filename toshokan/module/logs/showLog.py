# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 11:55:46 2021

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


def showLog():
    con = connect()
    cursor = con.cursor()
    
    cursor.execute("select * from log where in_date IS NULL OR in_date=''")
    
    results = cursor.fetchall()
    cursor.execute("SHOW columns FROM log")
    
    res = [column[0] for column in cursor.fetchall()]
    print(res)
           
    
    for row in results:
        print(row)
    
# showLog()

def showAll(idType, id_n, table):
    con = connect()
    cursor = con.cursor()
    
    cursor.execute(f"select * from {table} where {idType}=%s", (id_n,))
    
    row_count = cursor.rowcount
    if row_count <= 0:
        print("「図書は貸出されていません。")
    
    results = cursor.fetchall()
    print(row_count)
    for row in results:
        print(row)
    
    
showAll("c_id", 100, "customer")