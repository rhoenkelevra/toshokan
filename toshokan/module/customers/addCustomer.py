import mysql.connector as mydb

# 利用者一覧管理メニュー
# ２）新規登録
# 新規利用者を登録します


def addCustomer():
    conn = mydb.connect(
        host="localhost", port="3306", user="root", password="pass", database="toshokan"
    )
    
    # カーソルの作成
    cur = conn.cursor()
    
    
    """
    while True:
    # try:
        # 利用者登録を確認
        #登録する利用者名を入力
    #(1)利用者名
        n_name = input("利用者名を入力してください：")
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
            print("利用者名を入力してください：")
            
          
        # cur.execute("select * from customer where c_NAME =%s", (c_NAME,))
        # cur.fetchall()
        # # 利用者登録済み判定
        # if cur.rowcount > 0:
        #     # 書籍登録済みの場合は、登録処理を行わない
        #     # #利用者名の文字長　=< 20
        #     # #「利用者名の長さが最大値を超えています。」のエラーメッセージ合
        #     print("登録済み利用者です。")
        #     exit(0)
    """
    
    print("利用者の関連情報を入れてください。")
    
    # 未登録の場合#　名前が合格の時
    # 利用者情報を入力する
    n_name = input("必須：名前を入力してください：")
    n_name_kana = input("必須：カナ名を入力してください：")
    n_post_code = int(input("必須：郵便番号を入力してください："))  # DBを文字化する
    n_address = input("必須：住所を入力してください：")
    n_tel = input("必須：電話番号を入力してください：")
    n_email = input("任意：メールアドレスを入力してください：")
    n_memo = input("任意：記載欄：")
    
    
    # カスタマー情報を入力
    c_id = input("")
    data = (n_name, n_name_kana, n_post_code, n_address, n_tel, n_email, n_memo)
    
    # 利用者情報テーブルへの追加
    
    cur.execute(
        "insert into customer(c_name, c_name_kana, post_code, address, tel, email, memo) values(%s, %s, %s, %s, %s, %s, %s)",
        (data),
    )
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
