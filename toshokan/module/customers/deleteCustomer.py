def deleteCustomer():
    
    import datetime
    from module.setup.connect import connect
#機能　利用者の削除 deleteCustomer

    try:
    #接続
        conn = connect()
        cur = conn.cursor()
        
        
        print(" "*50)
        print("利用者の削除を行います。")
    
        
        #利用者名とID一覧表示(削除されたデータ以外表示)
        
        cur.execute("select c_name,c_id from customers where d_flag = 1 order by c_id")
        
        idlist = []
        
        rows = cur.fetchall()
        for row in rows:
            (rname,rid)= (row)
            idlist.append(rid)
        
        #削除を選択する　（削除するidを入力）
        
        print(f"現在の登録利用者 {idlist}")
        
        while True:
        
            try:
                did = int(input("利用者IDを入力してください。 \n>"))
                print(did)
                
                if did in idlist:
                    ddd = str(did)
    
                    break 
                     
                else:
                    print ("このIDは、利用者名簿に存在しません。　やり直して下さい。")   
            except ValueError:
                print("入力が間違ってます。　やり直してください。")
        
        #利用者削除確認へ遷移
        #選択したidで利用者の情報確認　
        
        cur.execute("select * from customers where c_id = %s",(did,))
        rows = cur.fetchall()
        for row in rows:
            (rid,rname,rnamekana,rpc,radd,rtel,remail,rqtybooks,rrdate,rddate,rmemo,rflg) = (row)
    #        print (row)
        
            print("削除する利用者情報 ")
            print("-"*60)
            print(f"利用者ID　:\t\t{rid}")
            print(f"利用者名 : \t\t{rname}")
            print(f"利用者名（カナ） :\t{rnamekana}")
    #            print(f"〒　 : \t{rpc}")
    #            print(f"住所 : \t{radd}")
    #            print(f"電話番号 : {rtel}")
    #            print(f"E-mail : {remail}")
    #            print(f"メモ : {rmemo}") 
            
        #利用者の借用状況（貸出数）        
        #選択した利用者が図書を借用中である？　
    
        if rqtybooks >= 1 :
            print("*"*60)
            print(f"警告！！！　利用者の現在の貸出数は {rqtybooks}　冊です。")
        #「図書借用中の利用者を削除できません。」表示
            print("図書借用中の利用者を削除できません。\n　すべて返却されてから削除してください。")
        #    print(f"返却督促先:電話　{rtel} E-mail {remail} ")
        
        else:
            
            confirm = input(f"{rname}さんを削除してよいですか？　(はい:y / いいえ:n) \n>")
            if confirm == "n":
                print("利用者削除を中止します。")
            else:
        #削除登録を選択する＝削除フラグ(d-flag)を0,delete_date を本日にする
                today = datetime.date.today()
                datetime_format = datetime.date.today()
                ddate = datetime_format.strftime("%Y%m%d")
    
                                
                cur.execute(f"update customers set delete_date = {ddate} where c_id = %s",(did,))
                cur.execute(f"update customers set d_flag = 0 where  c_id = %s",(did,))
                #正常に処理できた場合
                print(f"ID　{ddd} の 利用者　{rname} さんを削除しました。　")

    finally:
        conn.commit()
        cur.close()
    conn.close()
