def addCustomer():
    
#利用者一覧管理メニュー
#２）新規登録
#新規利用者を登録します

    from module.setup.connect import connect

    # コネクションの作成
    conn = connect()
    # カーソルの作成
    cur = conn.cursor()
    
    
    while True:
    # try:
        # 利用者登録を確認
        #登録する利用者名を入力
    #(1)利用者名
        n_name = input("利用者名を入力してください \n>")
            # #利用者名が入力された？
        print(n_name)
    
            # #利用者名の文字長　=< 20
            # #「利用者名の長さが最大値を超えています。」のエラーメッセージ合
        if n_name != "":
            if len(n_name)<=20:
                print("利用者名完了")
                break
            else:
                print("最大値を超えています")
    #「利用者名が入力されていません。」のエラーメッセージ        
        else:
            print("利用者名を入力されていません \n>")
            
    print("=" * 30)
    print(" " * 7,"新規利用者登録"," " * 7,)
    print("=" * 30)
    print("-" * 2,"利用者の関連情報を入れてください。","-" * 2,)
        
    #カナ名を入力
    n_name_kana = input("必須：カナ名を入力してください(20字以内) \n>")
    while n_name_kana == "":
        print("未入力です。")
        n_name_kana = input("再度カナ名を入れてください。\n>")
        
    import re
    
    while True:        
        re_katakana = re.compile(r'[\u30A1-\u30F4]+')
        status_kata = re_katakana.fullmatch(n_name_kana)        
        if status_kata:
                # Trueが返却される
            break
        else :
            n_name_kana = input("カタカナではありません。カナ名を入力してください \n>")
        
    while len(n_name_kana) > 20:
        print("カナ名の長さが最大値を超えています。")
        n_name_kana = input("カナ名を入力してください(20字以内)。\n>")                
    
        
    #郵便番号を入力
    while True:
        n_post_code = input("必須：郵便番号を入力してください \n>")
        if n_post_code:
            break
        else:
            print("入力がされていません。再入力してください。")
        
        
    #住所を入力   
    while True:
        n_address = input("必須：住所を入力してください \n>")
        if n_address:
            break
        else:
            print("入力がされていません。再入力してください。")
    

    #電話番号を入力
    while True:
        n_tel = input("必須：電話番号を入力してください \n>")
        if n_tel:
            break
        else:
            print("入力がされていません。再入力してください。")
    
    
    n_email = input("任意：メールアドレスを入力してください \n>")
    n_memo = input("任意：記載欄 \n>")
    
    
    # カスタマー情報をDBに書き込み
    c_id = input("")
    data = (n_name,n_name_kana,n_post_code,n_address,n_tel,n_email,n_memo)
    
    # 利用者情報テーブルへの追加
    
    cur.execute("insert into customers(c_name, c_name_kana, post_code, address, tel, email, memo) values(%s, %s, %s, %s, %s, %s, %s)", (data))
    # if cur.rowcount == 0:
    #         # 追加失敗
    #         raise Exception
                
                
        # 更新を確定する
    conn.commit()
    print("利用者情報を登録しました。")
    # except:
    #     conn.rollback()
    #     print("利用者情報の登録に失敗しました。")
    
    # カーソルの切断
    cur.close()
    
    # コネクションの切断
    conn.close()
    
#addCustomer()