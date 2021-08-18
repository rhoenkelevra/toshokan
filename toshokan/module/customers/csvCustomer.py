def csvCustomer():

    import csv
    import tkinter as tk #ファイル保管場所選択用に準備
    import tkinter.filedialog as fd #ファイル保管場所選択用に準備
    from module.setup.connect import connect

    root = tk.Tk()
    root.withdraw()
    data = []

#データベースからの読み込み    

    conn = connect()
    cur = conn.cursor()
    cur.execute("select c_id, c_name, c_name_kana, post_code, address, tel, email from customer where d_flag = 1 order by c_id")
    rows = cur.fetchall()

    for row in rows:
        
        (c_id, c_name, c_name_kana, post_code, address, tel, email) = (row)
        newdata =[str(c_id),c_name, c_name_kana, str(post_code), address, tel]
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
        title = [['利用者ID','利用者名','利用者名（カナ）', '〒', '住所', '電話番号', 'E-mail']]
        writer = csv.writer(f)
        writer.writerows(title)
    #CSV利用者表書き込み
        f = open(file, 'a', newline='')
        #data =[[str(c_id)],[c_name], [c_name_kana], [str(post_code)], [address], [tel]]
        #data = (row)
        writer = csv.writer(f)
        writer.writerows(data)
        f.close()
        print(f"CSVファイルを{file}に作成しました")
    except  FileNotFoundError :
        print ("CSVは作成せず、メニューに戻ります")

