#貸出回数が多い本をリストアップ

def optninki():
    
    from module.setup.connect import connect
    conn = connect()    
    
    # カーソルの作成
    cur = conn.cursor()
        
    #貸出回数一覧表示（貸出記録から貸出回数が多い順にリストアップします。）

    print(" "*60)
    print("人気本一覧表")
    print("貸出記録から貸出回数が多い順にリストアップします。")
    print("="*60)
    print("借用回数 \t図書名")
    print("="*60)


    cur.execute("select count(logs.out_date),books.title,logs.b_id from logs left join books on logs.b_id = books.b_id group by b_id order by 1 desc")
    rows = cur.fetchall()

    # 実行結果の表示
    for row in rows:
        (kaisu,bname,bid)= row

        
        print(f"\t{kaisu}\t:{bname}")


    cur.close()
    conn.close()
    


