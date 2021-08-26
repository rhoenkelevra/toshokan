from module.setup.connect import connect
import re

def ShowCustomerData(row):

    print("=" * 60)
    print("利用者ID:\t\t" + str(row[0][0]))
    print("利用者名:\t\t" + str(row[0][1]))
    print("利用者名（カナ）:\t" + str(row[0][2]))
    print("〒:\t\t\t" + str(row[0][3]))
    print("住所:\t\t\t" + str(row[0][4]))
    print("電話番号:\t\t" + str(row[0][5]))
    print("E-mail:\t\t\t" + str(row[0][6]))
    print("メモ:\t\t\t\t" + str(row[0][10]))
    print("=" * 60)


def updateCustomer(): 

    try:

        # コネクションの作成
        conn = connect()
        cur = conn.cursor()

        while True:

            try:
                c_id = int(input("利用者IDを入力してください。　（00　終了） \n> "))

            except ValueError:
                print("数字で入力してください。")
                continue


            if c_id == 00:
                break

            else:
                # 変更・更新したい利用者の情報を表示する
                cur.execute("SELECT * from customers where c_id = %s", (c_id,))
                row = cur.fetchall()
                
                # 削除済みの利用者は変更できない
                if row[0][11] == 0:
                    print("この利用者は既に削除されています。")
                
                else:
                    # 利用者情報を表示させる
                    ShowCustomerData(row)

                    check = input("この利用者を変更しますか？ (はい:y / いいえ:n)\n> ")

                    if check == "y":
                        while True:
                            try:
                                print("\n変更する項目の番号を入力ください。 (終了 00)")
                                inp = int(input("1: 利用者名\n2: 利用者名（カナ）\n3: 〒\n4: 住所\n5: 電話番号\n6: E-mail\n7: メモ\n> "))

                                # 1: 利用者名の変更
                                if inp == 1:
                                    while True:
                                        c_name = input("変更内容を入力してください。\n>")
                                        if c_name == "":
                                            print("利用者名が入力されていません。")
                                            continue
                                        if len(c_name) > 40:
                                            print("利用者名の長さが最大値を超えています。")
                                            continue
                                        break
    
                                    data = (c_name, c_id)
                                    cur.execute(
                                        "UPDATE customers set c_name = %s where c_id = %s", data)
                                
                                # 2: 利用者名（カナ）の変更
                                elif inp == 2:
                                    while True:
                                        c_name_kana = input("変更内容を入力してください。\n>")
                                        if c_name_kana == "":
                                            print("利用者名（カナ）が入力されていません。")
                                            continue
    
                                        if len(c_name_kana) > 50:
                                            print("利用者名（カナ）は50字以内で入力してください。")
                                            continue
                                        
                                        if re.compile(r'[\u30A1-\u30F4　 ]+').fullmatch(c_name_kana) == None:
                                            print("カナで入力してください。")
                                            continue
                                        break
    
                                    data = (c_name_kana, c_id)
                                    cur.execute(
                                        "UPDATE customers SET c_name_kana = %s where c_id = %s", data)
                                    row = cur.fetchone()
    
                                # 3: 郵便番号の変更
                                elif inp == 3:
                                    while True:
                                        post_code = input("変更内容を入力してください。\n>")
                                        if post_code == "":
                                            print("郵便番号が入力されていません。")
                                            continue
                                        if re.compile(r'^[0-9-]+$').fullmatch(post_code) == None:
                                            print("入力できる文字は半角数字および ”-” です。")
                                            continue
                                        if re.compile(r'^[0-9]{3}-[0-9]{4}$').fullmatch(post_code) == None:
                                            print("入力できる文字は半角数字および ”-” です。(例:000-0000)")
                                            continue

                                        break
                                    
                                    data = (post_code, c_id)
                                    cur.execute(
                                        "UPDATE customers set post_code = %s where c_id = %s", data)
                                    row = cur.fetchone()   
    
    
                                #　4: 住所の変更
                                elif inp == 4:
                                    while True:
                                        address = input("変更内容を入力してください。\n>")
                                        if address == "":
                                            print("住所が入力されていません。")
                                            continue
                                        break
    
                                    data = (address, c_id)                          
                                    cur.execute(
                                        "UPDATE customers set address = %s where c_id = %s", data)
                                    row = cur.fetchone()
                                
                                #　5: 電話番号の変更
                                elif inp == 5:
                                    while True:
                                        tel = input("変更内容を入力してください。\n>")
                                        if tel == "":
                                            print("電話番号が入力されていません。")
                                            continue
                                        if re.compile(r'^[0-9-]+$').fullmatch(tel) == None:
                                            print("入力できる文字は半角数字および ”-” です。")
                                            continue
                                        break
                                    
                                    data = (tel, c_id)
                                    cur.execute(
                                        "UPDATE customers set tel = %s where c_id = %s", data)
                                    row = cur.fetchone()
    
                                #　6: e-mailの変更
                                elif inp == 6:
                                    while True:
                                        email = input("変更内容を入力してください。\n>")
                                        if email == "":
                                            print("E-mailが入力されていません。")
                                            continue
                                        if re.compile(r'^[a-zA-Z0-9.!-/:-@[-`{-~]+$').fullmatch(email) == None:
                                            print("入力できる文字は半角数字および半角記号のみです。")
                                            continue
                                        break
                                    
                                    data = (email, c_id)
                                    cur.execute(
                                        "UPDATE customers set email = %s where c_id = %s", data)
                                    row = cur.fetchone()
    
                                #　7: メモの変更
                                elif inp == 7:
                                    memo = input("変更内容を入力してください。\n>")

                                    data = (memo, c_id)
                                    cur.execute(
                                        "UPDATE customers set memo = %s where c_id = %s", data)
                                    row = cur.fetchone()
    
    
                                else:
                                    print("利用者情報の変更を中止しました。")
                                    break

                                #この内容でよろしいですか？　(y/n)
                                inp = input("この変更内容でよろしいですか？ (はい:y / いいえ:n)\n> ")
                                if inp == "y":
    
                                    # SQLに登録完了
                                    conn.commit()
                                    cur.execute("SELECT * from customers where c_id = %s",(c_id,))
                                    row = cur.fetchall()
                                    print("変更しました。")
    
                                    ShowCustomerData(row)
    
                                else:
                                    print("変更登録を中止しました.")
                                    conn.rollback()

                                break

                            except ValueError:
                                print("数字で入力してください。")
                                continue

                    # noを入力した時は登録処理は中止する
                    else:
                        print("変更登録を中止しました。")
            
    except:
        print("エラーになりました。")
        
    finally:
        cur.close()
        conn.close()
    
# updateCustomer()