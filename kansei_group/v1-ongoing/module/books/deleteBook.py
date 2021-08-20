from module.setup.connect import connect

def deleteBook(): 

    # コネクションの作成
    conn = connect()
    cur = conn.cursor()
    
    while True:
        try:
            b_id = int(input("図書IDを入力してください。　（00　終了） \n> "))

            if b_id ==00:
                break
            
            data = (b_id,)
            cur.execute("SELECT * from books where b_id = %s", data)
            row = cur.fetchall()

            if cur.rowcount > 0:
                
                if row[0][7] == 0:
                    print("この図書は既に削除されています。")
                
                else:   
                    p_date = str(row[0][5])
        
                    print("=" * 60)
                    print("図書ID:".ljust(9) + str(row[0][0]))
                    print("isbn:".ljust(11) + str(row[0][1]))
                    print("図書名:".ljust(8) + str(row[0][2]))
                    print("著者名:".ljust(8) + str(row[0][3]))
                    print("出版社:".ljust(8) + str(row[0][4]))
                    print("出版日:".ljust(8) + str(p_date.replace('-','/')))
                    print("=" * 60)
                    
                    inp = input("この図書を削除しますか？ (はい:y / いいえ:n)\n> ")
                    
                    # 図書を削除登録する
                    if inp == "y":
                        
                        # 貸出可の図書なら処理を進める
                        if row[0][6] == 1:
                           
                            # ｓｔａｔｕｓを-1する
                            cur.execute("UPDATE books set status = status -1 where b_id = %s",(b_id,))
                            # d_flagを-1する
                            cur.execute("UPDATE books set d_flag = d_flag -1 where b_id = %s",(b_id,))
                                
                            print(f"図書「{row[0][2]}」を削除しました。")
                            conn.commit()
                        
                        # 貸出中の図書の場合は削除不可
                        else:
                            print("貸出中の図書を削除できません。")
                
                    # noを入力した時は登録処理は中止する
                    else:   
                        print("削除登録を中止しました。")

            # 図書IDが未登録
            else:
                print("未登録です。")

        # 図書IDの入力エラー
        except ValueError:
            print("数字で入力してください。")
            continue
        # 図書IDの入力エラー
        except Exception:
            print("エラーが発生しました。中止します。")
           
                        
    cur.close()
    conn.close()
    
deleteBook() 
