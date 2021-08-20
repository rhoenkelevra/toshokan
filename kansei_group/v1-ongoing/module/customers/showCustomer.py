def showCustomer():


    import pprint  #表示整えるために準備
    
    from module.setup.connect import connect
    conn = connect()
    
    cur = conn.cursor()
    

    print("利用者一覧表")
    print(" "*50)
    #利用者一覧表示(削除されたデータ以外表示)
    
    print("利用者ID ","利用者名 ","利用者名（カナ） ", "〒 ", "住所 ", "電話番号 ", "E-mail ")
    
    print("--"*25)
    cur.execute("select c_id, c_name, c_name_kana, post_code, address, tel, email from customers where d_flag = 1 order by c_name")
    rows = cur.fetchall()
    
    for row in rows:
        
        (c_id, c_name, c_name_kana, post_code, address, tel, email) = (row)
        print(str(c_id),c_name, c_name_kana, str(post_code), address, tel,email)

    print("-"*50)
    print(" "*50)
    print("別形式で表示します。")
    print("--"*25)
    for row in rows:
        
        print("=" * 50)
        print(f"利用者IDD:\t\t{row[0]}")
        print(f"利用者名:\t\t{row[1]}")
        print(f"利用者名（カナ）:\t{row[2]}")
        print(f"〒     :\t\t\t{row[3]}")
        print(f"住所    :\t\t{row[4]}")
        print(f"電話番号:\t\t{row[5]}")        
        print(f"E-mail :\t\t{row[6]}") 
