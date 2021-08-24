def addCustomer():
    
#利用者一覧管理メニュー
#２）新規登録
#新規利用者を登録します

    from module.setup.connect import connect
    import re
    
    try:
        # コネクションの作成
        conn = connect()
        # カーソルの作成
        cur = conn.cursor()
    
        while True:
        # try:
            # 利用者登録を確認
            #登録する利用者名を入力
        #(1)利用者名長野
            n_name = input("利用者名を入力してください。(20字以内）(00 終了) \n>")
                # #利用者名が入力された？
                
        # 利用者登録の終了
            if n_name == "00":
                print("登録を終了しました。")
                return

                # #利用者名の文字長　=< 20
                # #「利用者名の長さが最大値を超えています。」のエラーメッセージ合
            if n_name != "":
    
                if len(n_name)<=20:
                    break
                
                
                else:
                    print("利用者名の長さが最大値を超えています。")
        #「利用者名が入力されていません。」のエラーメッセージ        
            else:
                print("利用者名が入力されていません。 \n>")
                
        print("=" * 60)
        print(" " * 22,"新規利用者登録"," " * 22,)
        print("=" * 60)
        print("" * 60)    
        print("利用者の関連情報を入力してください。")
            
        #カナ名を入力
        n_name_kana = input("カナ名を入力してください。(50字以内) \n>")
        while n_name_kana == "":
            print("未入力です。")
            n_name_kana = input("カナ名を入力してください。(50字以内) \n>")
    
    
        while True:        
            re_katakana = re.compile(r'[\u30A1-\u30F4　 ]+')
            status_kata = re_katakana.fullmatch(n_name_kana)        
            if status_kata:
                    # Trueが返却される
                break
            else :
                n_name_kana = input("カタカナではありません。 \n>")
            
        while len(n_name_kana) > 50:
            print("カナ名の長さが最大値を超えています。")
            n_name_kana = input("カナ名を入力してください。(50字以内)\n>")                
        
            
        #郵便番号を入力(d/d/d形式)
        
        while True:
            n_post_code = input("郵便番号(000-0000)を入力してください \n>")
            
            post_format = re.search("\d\d\d[-]\d\d\d\d", n_post_code)
            
            if post_format == True:
                break
            else:
                print("入力できる郵便番号は、半角数字および”-”のみです。(例:000-0000)")    
            
            
        #住所を入力   
        while True:
            n_address = input("住所を入力してください。 \n>")
            if n_address:
                break
            else:
                print("入力されていません。")
            
        while True:
            n_tel = input("電話番号を入力してください。 \n>")
            tel_format = re.compile(r'^[0-9-]+$')
            tel_status = tel_format.fullmatch(n_tel)
            
            if tel_status:
                break
            else:
                print("入力できる電話番号は、半角数字および”-”のみです。")
    
        while True:
            n_email = input("メールアドレスを入力してください。（任意） \n>")
            email_format = re.compile(r'^[a-zA-Z0-9.!-/:-@[-`{-~]+$')
            email_status = email_format.fullmatch(n_email)
            
            if n_email == "":
                break
            
            if email_status:
                break
            
            else:
                print("入力できるメールアドレスは、半角英数字および半角記号のみです。")
        
        n_memo = input("メモを入力してください。（任意） \n>")
        
        # カスタマー情報をDBに書き込み
        data = (n_name,n_name_kana,n_post_code,n_address,n_tel,n_email,n_memo)
        print()
        
        # #入力内容表示
        # print("=" * 50)
        # print("利用者名:".ljust(10) + str(n_name))
        # print("利用者名:".ljust(10) + str(n_name_kana))
        # print("郵便番号".ljust(10) + str(n_post_code))        
        # print("住所:".ljust(14) + str(n_address))
        # print("電話番号:".ljust(10) + str(n_tel))
        # print("E-mail（任意）:".ljust(10) + str(E-mail))
        # print("メモ（任意）:".ljust(10) + str(n_memo))        
        # print("=" * 50)
        
        # inp = input("この内容で登録してよろしいですか？( はい：y / いいえ：n )\n>")
        
        # condition = True
        # while condition == True:
        #     if inp != "y":
        #         return
            
        #     # 変数へ代入し、logsテーブルへデータ挿入
        #     try:
    
        
        # 利用者情報テーブルへの追加
        cur.execute("insert into customers(c_name, c_name_kana, post_code, address, tel, email, memo) values(%s, %s, %s, %s, %s, %s, %s)", (data))
        # if cur.rowcount == 0:
        #         # 追加失敗
        #         raise Exception
            
            # 更新を確定する
    
    #        cur.excute("select c_name,c_name_kana,c_post_code,c_address,c_tel,c_email,c_memo from customer where c_name = %s,(n_name,)")
    #        rows = cur.fetchall()
    #        for row in rows:
        cur.execute("select c_id, c_name, c_name_kana, post_code, address, tel, email, memo from customers where c_name = %s",(n_name,))
        rows = cur.fetchall()
    
        for row in rows:
            print("=" * 60)
    #        print("利用者ID:.ljust(13) + {row[0]}")
            print(f"利用者ID\t:{row[0]}")
            print(f"利用者名\t:{row[1]}")
            print(f"利用者名（カナ）:{row[2]}")
            print(f"〒   \t\t:{row[3]}")
            print(f"住所 \t\t:{row[4]}")
            print(f"電話番号 \t:{row[5]}")        
            print(f"E-mail\t\t:{row[6]}") 
            print(f"メモ    \t:{row[7]}")
            print("=" * 60)        
        conf=input("この内容で確定してよろしいですか。　はい:y いいえ:n \n>")
        if conf == "y":
            conn.commit()
            print("利用者情報を登録しました。")
        else:
                print("登録中止します。")
    except:
            print("登録失敗しました。")
            
    
    
        #    print(f{"n_name"さんのIDは""です。})
            # except:
            #     conn.rollback()
            #     print("利用者情報の登録に失敗しました。")
    finally:
        # カーソルの切断
        cur.close()
        
        # コネクションの切断
        conn.close()
        
# addCustomer()