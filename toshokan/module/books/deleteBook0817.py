from module.setup.connect import connect

def deleteBook(): 

    conn = connect()
    cur = conn.cursor()
    
    while True:
            
        try:
            b_id = int(input("図書IDを入力してください。　（00　終了） \n> "))
    
        except ValueError:
            print("数字で入力してください。")
            continue
        except Exception:
            print("エラーが発生しました。")

    
        if b_id == 00:
            print("終了しました。")
            break 
    
        else:
            # 削除したい図書の情報を表示する
            cur.execute("SELECT * from books where b_id = %s", (b_id,))
            row = cur.fetchall()
            p_date = str(row[0][5])

            print("=" * 50)
            print(f"<図書ID>  {row[0][0]}")
            print(f"<isbn>    {row[0][1]}")
            print(f"<図書名>  {row[0][2]}")
            print(f"<著者名>  {row[0][3]}")
            print(f"<出版社>  {row[0][4]}")
            print(f"<出版日>  {p_date.replace('-','/')}")
            print("=" * 50)
        
    
        # 削除済みのデータだった場合
        if row[0][7] == 0:
            print("この図書は既に削除されています。")

        else:   
            inp = input("この図書を削除しますか？ (はい:y / いいえ:n)\n> ")
            
        
            if inp == "y":
    
                # 貸出可の図書を削除登録する
                if row[0][6] == 1:
                       
                    # ｓｔａｔｕｓを-1する
                    cur.execute("UPDATE books set status = status -1 where b_id = %s",(b_id,))
                    # d_flagを-1する
                    cur.execute("UPDATE books set d_flag = d_flag -1 where b_id = %s",(b_id,))
                        
                    print(f"図書{row[0][2]}を削除しました。")
                    conn.commit()
                    
                    # 貸出中の図書の場合は削除不可
                else:
                    print("貸出中の図書は削除できません。")
                
            
            # noを入力した時は登録処理は中止する
            else:
                print("削除登録を中止しました。")
            
                        
    cur.close()
    conn.close()


# =============================================================================
# 実行
# =============================================================================
deleteBook()

