# csvファイル名を取得する関数を定義（csvBook_lending関数で使用）
def getfilename():
    
    import tkinter as tk
    import tkinter.filedialog as fd

    # tkアプリウインドウを表示しない
    root = tk.Tk()
    root.withdraw()
    
    # 保存ダイアログを表示する
    file = fd.asksaveasfilename(
        initialfile = "booklendinglist.csv",
        defaultextension = ".csv",
        title = "保存場所を選んでください。",
        filetypes = [("CSV", ".csv")]
    )
    return file

def csvBook_lending():
    from module.setup.connect import connect
    import csv

    # コネクションの作成
    conn = connect()
    
    # カーソルの作成
    cur = conn.cursor()
    
    # データベースからd_flagが1(=図書が存在している)を取得
    cur.execute(
        """
        select books.b_id, isbn, title, author, p_name, p_date, in_limit_date
         from books inner join logs on books.b_id = logs.b_id
         where books.d_flag = 1 and books.status = 0
         """
        )
    rows = cur.fetchall()
    
    if cur.rowcount != 0:
        try:
            # csvのファイル名を取得
            file = getfilename()
    
            # csvに表示したい項目名を設定
            header = ["図書ID", "isbn", "図書名", "著者名", "出版社", "出版日", "貸出期限"]

            # csvに項目名とデータベース取得結果を出力
            with open(file, "a", encoding = "shift_jis", newline="") as f:
                fileobj = csv.writer(f)
                fileobj.writerow(header)
                for row in rows:
                    fileobj.writerow(row)
                    
            print(f"CSVファイルを{file}に出力しました。")

        except Exception:
            print("CSV出力を中止しました。")

    else:
        print("貸出中の図書はありません。")

    # カーソルの切断
    cur.close()
    # コネクションの切断
    conn.close()

