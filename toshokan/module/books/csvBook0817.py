# csvファイル名を取得する関数を定義（csvBook関数で使用）
def getfilename():
    
    import tkinter as tk
    import tkinter.filedialog as fd
    from module.setup.connect import connect

    # tkアプリウインドウを表示しない
    root = tk.Tk()
    root.withdraw()
    
    # 保存ダイアログを表示する
    file = fd.asksaveasfilename(
        initialfile = "booklist.csv",
        defaultextension = ".csv",
        title = "保存場所を選んでください。",
        filetypes = [("CSV", ".csv")]
    )
    return file

def csvBook():
    import csv
    import pandas as pd
    import mysql.connector as mydb

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
    
    # csvのファイル名を取得
    file = getfilename()
    
    # csvに表示したい項目名を設定
    header = ["図書ID", "isbn", "図書名", "著者名", "出版社", "出版日", "貸出状況"]

    # csvに項目名とデータベース取得結果を出力
    with open(file, "a", encoding = "shift_jis", newline="") as f:
        fileobj = csv.writer(f)
        fileobj.writerow(header)        
        for row in rows:
            fileobj.writerow(row)            

    # 一度保存したcsvを読み込み
    read_file = pd.read_csv(file, encoding="shift-jis")

    # 「貸出状況」の項目について、0:貸出中、1:空欄　へ置換
    read_file = read_file.replace({"貸出状況":{0: "貸出中", 1: "貸出可"}})

    # 置換したデータをcsvへ出力
    write_file = pd.DataFrame(read_file)
    write_file.to_csv(file, encoding="shift-jis", index=False)

    # カーソルの切断
    cur.close()
    # コネクションの切断
    conn.close()

# =============================================================================
# 実行 
# =============================================================================

