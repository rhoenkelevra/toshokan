def csvCustomer():

    import csv
    import tkinter as tk #ファイル保管場所選択用に準備
    import tkinter.filedialog as fd #ファイル保管場所選択用に準備
    from module.setup.connect import connect
    try:
        root = tk.Tk()
        root.withdraw()
        data = []
    
    #データベースからの読み込み    
    
        conn = connect()
        cur = conn.cursor()
        cur.execute("select c_id, c_name, c_name_kana, post_code, address, tel, email,qtybooks,register_date,delete_date,memo from customers order by c_id")
        rows = cur.fetchall()
    
        for row in rows:
            
            (c_id, c_name, c_name_kana, post_code, address, tel, email,qtybooks,register_date,delete_date,memo) = (row)
            newdata =[str(c_id),c_name, c_name_kana, str(post_code), address, tel, email, qtybooks,register_date,delete_date,memo ]
            data.append(newdata)
    
        try:
    #CSV保存先指定
            file = fd.asksaveasfilename(
                initialfile = "customerlist", 
                defaultextension = ".csv", 
                title = "保存場所を選んでください。", 
                filetype = [("CSV", ".csv")]
            )
        
    
        #CSVタイトル書き込み
            f = open(file, 'a', newline='')
            title = [['利用者ID','利用者名','利用者名（カナ）', '〒', '住所', '電話番号', 'E-mail','貸出冊数','利用者登録日','利用者削除日','メモ']]
            writer = csv.writer(f)
            writer.writerows(title)
        #CSV利用者表書き込み
            f = open(file, 'a', newline='')
    
            writer = csv.writer(f)
            writer.writerows(data)
            f.close()
            print(f"CSVファイルを{file}に出力しました。")
        except  FileNotFoundError :
            print ("CSV出力を中止しました。")
        except PermissionError :
            print("ファイルは使用中で、CSV出力を中止しました。")
    finally :
        conn.commit()
        cur.close()
        conn.close()

