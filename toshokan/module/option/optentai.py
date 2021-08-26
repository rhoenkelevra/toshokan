#延滞者・本をリストアップ
def optentai():
    
    import datetime
    from module.setup.connect import connect
    conn = connect()    
    
    # カーソルの作成
    cur = conn.cursor()
    
    entai = []
    #本日はいつ？
    today = datetime.date.today()
    
    #延滞一覧表示（科返却期日が本日から３日以前が延滞対象　３日の督促猶予）
    print(" "*50)
    print("延滞督促一覧表")
    print("返却期日が本日から３日より前が延滞対象です")
    
    #本日から３日前の日を特定し、それより前の貸出日ログを検索
    ddate = today + datetime.timedelta(days=-3)
    data = (ddate, )
    
    cur.execute("select out_date,b_id,c_id, in_limit_date from logs where in_date is null and in_limit_date <  %s" ,data)
    
    # 実行結果を取得
    rows = cur.fetchall()
    
    if cur.rowcount > 0:
        # 実行結果の表示
        for row in rows:
            (out_date,bid,cid, in_limit_date)= row
            entai.append(row)
    #延滞されている書名を検索
            datab = (bid,)
            cur.execute("select title from books where b_id = %s" ,datab)
            rows = cur.fetchall()
            for row in rows:
                ebook = row[0]
    #延滞している利用者情報を検索
            datac = (cid,)
            cur.execute("select c_name,tel,email from customers where c_id = %s" ,datac)
            rows = cur.fetchall()
            for row in rows:
                (ecust,etel,eemail) = row
                print("="*60)
                odate = str(out_date)
                ldate = str(in_limit_date)
                print(f"貸出日\t\t:{odate.replace('-','/')}") 
                print(f"返却期限日\t:{ldate.replace('-','/')}") 
                print(f"利用者\t\t:{ecust}")
                print(f"延滞書名\t:{str(ebook)}")
                print(f"督促先\t\t:TEL:{etel}  E-mail {eemail}")
                print("="*60)
    else:
        print("督促対象の延滞はありません。")
    
    # カーソルの切断
    cur.close()
    # コネクションの切断
    conn.close()
    
# optentai()
