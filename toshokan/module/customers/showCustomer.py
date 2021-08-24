def showCustomer():


    import pprint  #表示整えるために準備
    
    from module.setup.connect import connect

    try:
        conn = connect()
        cur = conn.cursor()
    
        print(" "*60)
        print("利用者一覧表(現在の登録者)")
    
        #利用者一覧表示(削除されたデータ以外表示)
    #    print("利用者ID ","利用者名 ","利用者名（カナ） ", "〒 ", "住所 ", "電話番号 ", "E-mail ")
        
        print("-"*60)
        cur.execute("select c_id, c_name, c_name_kana, post_code, address, tel, email, memo from customers where d_flag = 1 order by c_id")
        rows = cur.fetchall()
        
        for row in rows:
            
            (c_id, c_name, c_name_kana, post_code, address, tel, email,memo) = (row)

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
    finally:
        conn.commit()
        cur.close()
        conn.close()

