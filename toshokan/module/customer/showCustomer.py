# def showCustomer:
    

import csv
import mysql.connector as mydb
import tkinter as tk #ファイル保管場所洗濯用に準備
import tkinter.filedialog as fd #ファイル保管場所洗濯用に準備
import pprint#表示整えるために準備v


data = []

#def getdata():
    
conn = mydb.connect(
host="localhost",
port="3306",
user="user",
password="pass",
database="toshokan"
)

cur = conn.cursor()

try:
        
    print("利用者一覧表")
    print(" "*50)
    #利用者一覧表示(削除されたデータ以外表示)
    
    cshow = int(input("利用者一覧表　画面表示　1, CSV作成 2  終了　その他　\n>"))
    print(" "*50)
    
    if cshow == 1:
        print("利用者ID ","利用者名 ","利用者名（カナ） ", "〒 ", "住所 ", "電話番号 ", "E-mail ")
    
        print("--"*25)
        cur.execute("select c_id, c_name, c_name_kana, post_code, address, tel, email from customer where d_flag = 1 order by c_name")
        rows = cur.fetchall()
        
        for row in rows:
            
            (c_id, c_name, c_name_kana, post_code, address, tel, email) = (row)
            print(str(c_id),c_name, c_name_kana, str(post_code), address, tel,email)
            
    
    
    elif cshow == 2:
        cur.execute("select c_id, c_name, c_name_kana, post_code, address, tel, email from customer where d_flag = 1 order by c_name")
        rows = cur.fetchall()
        f = open('csvtest1.csv', 'w', newline='')
        title = [['利用者ID','利用者名','利用者名（カナ）', '〒', '住所', '電話番号', 'E-mail']]
        
        writer = csv.writer(f)
        writer.writerows(title)
        
        for row in rows:
            
            (c_id, c_name, c_name_kana, post_code, address, tel, email) = (row)
            newdata =[str(c_id),c_name, c_name_kana, str(post_code), address, tel]
            data.append(newdata)
            
            f = open('csvtest1.csv', 'w', newline='')
            #title = [['c_id','c_name','c_name_kana', 'post_code', 'address', 'tel', 'email']]
            title = [['利用者ID','利用者名','利用者名（カナ）', '〒', '住所', '電話番号', 'E-mail']]
            writer = csv.writer(f)
            writer.writerows(title)
            
            f = open('csvtest1.csv', 'a', newline='')
            #data =[[str(c_id)],[c_name], [c_name_kana], [str(post_code)], [address], [tel]]
            #data = (row)
            writer = csv.writer(f)
            writer.writerows(data)
            f.close()
    else:
        print("メニューに戻ります")
except :
        print("メニューに戻ります")
        
#return