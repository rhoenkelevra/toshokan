def deleteCustomer():
    
    from module.setup.connect import connect
#機能　利用者の削除 deleteCustomer

#接続


    conn = connect()
    cur = conn.cursor()
    
    print("利用者の削除を行います。")
    print(" "*50)
    
    #利用者名とID一覧表示(削除されたデータ以外表示)
    
    cur.execute("select c_name,c_id from customers where d_flag = 1 order by c_name_KANA")
    
    """
    名前から検索する場合の準備
    
    #削除する利用者を選択（利用者名検索　）
    dname = input ("削除する利用者名を入れてください。 \n>")
    
    cur.execute("select * from customers where c_name =%s,dname")
    
    """
    
    print("登録利用者名とIDの一覧を表示します。　（削除する利用者のIDを選択してください")
    print(" "*50)
    
    idlist = []
    
    rows = cur.fetchall()
    for row in rows:
        (rname,rid)= (row)
        print (f"利用者名:　{rname},　　　利用者ID: {rid} ")
        
        idlist.append(rid)
    
    #削除を選択する　（削除するidを入力）
    
    print(idlist)
    
    while True:
    
        try:
            did = int(input("選択した削除するIDを入力してください。 \n>"))
            print(did)
            
            if did in idlist:
                did = (did,)
                break 
                 
            else:
                print ("このIDは、利用者名簿に存在しません。　やり直して下さい。")   
        except ValueError:
            print("入力が間違ってます。　やり直してください。")
    
    #利用者削除確認へ遷移
    #選択したidで利用者の情報確認　
    
    cur.execute("select * from customers where c_id = %s",did)
    rows = cur.fetchall()
    for row in rows:
        (rid,rname,rnamekana,rpc,radd,rtel,remail,rqtybooks,rrdate,rddate,rmemo,rflg) = (row)
    #    print (row)
    
        print(f"削除する利用者情報　 \n 利用者ID　:　{rid} \n 利用者名　:{rname} \n 利用者名（カナ） :{rnamekana} \n")  
    #利用者の借用状況（貸出数）
    
    
    #選択した利用者が図書を借用中である？　
    
    if rqtybooks >= 1 :
        print(f"警告！！！　利用者の現在の貸出数は {rqtybooks}　冊です。")
    #「図書借用中の利用者を削除できません。」表示
        print("図書借用中の利用者を削除できません。\n　すべて返却されてから削除してください。")
    #    print(f"返却督促先:電話　{rtel} E-mail {remail} ")
    
    else:
        
        confirm = int(input(f"本当に{rname}さんを削除してよいですか？　１　で削除　 0　で中止します。 \n>"))
        if confirm == 0:
            print("利用者削除を取りやめてメインメニューに戻ります。")
        else:
    #削除登録を選択する＝削除フラグ(d-flag)を0にする
            cur.execute("update customers set d_flag = 0 where c_id = %s",did)
    #    print(cur.rowcount,"件、削除しました。")
    #正常に処理できた場合
            print(f"利用者　{rname} を削除しました。　\n メインメニューに戻ります。")
    
    #「利用者～を削除しました。」を表示。
    #やり直し
    conn.commit()
    cur.close()
    conn.close()
    



