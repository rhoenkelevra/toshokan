from module.setup.connect import connect

def showBook():

    conn = connect()
   

    # カーソルの作成
    cur = conn.cursor()

    # データベースからd_flagが1(=図書が存在している)を取得
    cur.execute("select b_id, isbn, title, author, p_name, p_date, status from books where d_flag = 1")
    rows = cur.fetchall()
    
    # 図書情報の表示
    for row in rows:
        print("=" * 20)
        print(f"<図書ID>   {row[0]}")
        print(f"<isbn>    {row[1]}")
        print(f"<図書名>  {row[2]}")
        print(f"<著者名>  {row[3]}")
        print(f"<出版社>  {row[4]}")
        print(f"<出版日>  {row[5]}")
        
        if row[6] == 0:
            print("<貸出状況>  貸出中")
        else:
            print("<貸出状況>  貸出可")
                
        print("=" * 20)
     
    # カーソルの切断
    cur.close()
    # コネクションの切断
    conn.close()


# =============================================================================
# 実行 
# =============================================================================
showBook()

