def showBook():

    import csv    
    import mysql.connector as mydb
    import tkinter as tk
    import tkinter.filedialog as fd


    # コネクションの作成
    conn = mydb.connect(
        host = "localhost",
        port = "3306",
        user = "root",
        password = "pass",
        database = "toshokan"
    ) 

    # カーソルの作成
    cur = conn.cursor()

    # データベースからd_flagが1(=図書が存在している)を取得
    cur.execute("select b_id, isbn, title, author, p_name, p_date, status from books where d_flag = 1")
    rows = cur.fetchall()
    
    # # tkアプリウインドウを表示しない
    root = tk.Tk()
    root.withdraw()
    
    # # 保存ダイアログを表示する
    file = fd.asksaveasfilename(
        initialfile = "booklist.csv",
        defaultextension = ".csv",
        title = "保存場所を選んでください。",
        filetypes = [("CSV", ".csv")]
    )

    # csvに表示したい項目名を設定
    header = ["図書ID", "isbn", "図書名", "著者名", "出版社", "出版日", "貸出状況"]

    # csvに項目名とデータベース取得結果を出力
    with open(file, "a", encoding = "shift_jis", newline="") as f:
        fileobj = csv.writer(f)
        fileobj.writerow(header)        
        for row in rows:
            fileobj.writerow(row)
   

    # カーソルの切断
    cur.close()
    # コネクションの切断
    conn.close()


# =============================================================================
# 実行 
# =============================================================================
showBook()

