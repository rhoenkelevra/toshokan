from module.setup.connect import connect

def showBook():
    # コネクションの作成
    conn = connect()
    
    # カーソルの作成
    cur = conn.cursor()

    # データベースからd_flagが1(=図書が存在している)を取得
    cur.execute("select b_id, isbn, title, author, p_name, p_date, status from books where d_flag = 1")
    rows = cur.fetchall()
    
    # 図書情報の表示
    for row in rows:
        print("=" * 60)
        print("図書ID:".ljust(9) + str(row[0]))
        print("isbn:".ljust(11) + str(row[1]))
        print("図書名:".ljust(8) + str(row[2]))
        print("著者名:".ljust(8) + str(row[3]))
        print("出版社:".ljust(8) + str(row[4]))
        print("出版日:".ljust(8) + str(row[5]).replace('-','/'))
        
        if row[6] == 0:
            print("貸出状況:".ljust(7) + "貸出中")
        else:
            print("貸出状況:".ljust(7) + "貸出可")
                
        print("=" * 60)
     
    # カーソルの切断
    cur.close()
    # コネクションの切断
    conn.close()