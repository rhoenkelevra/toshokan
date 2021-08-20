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
        print("=" * 50)
        print(f"図書ID:\t\t{row[0]}")
        print(f"isbn:\t\t{row[1]}")
        print(f"図書名:\t\t{row[2]}")
        print(f"著者名:\t\t{row[3]}")
        print(f"出版社:\t\t{row[4]}")
        print(f"出版日:\t\t{row[5]}")
        
        if row[6] == 0:
            print("貸出状況:\t貸出中")
        else:
            print("貸出状況:\t貸出可")
                
        print("=" * 50)
     
    # カーソルの切断
    cur.close()
    # コネクションの切断
    conn.close()