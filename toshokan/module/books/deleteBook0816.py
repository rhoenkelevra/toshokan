import re

def deleteBook(): 

    import mysql.connector as mydb

    # コネクションの作成
    conn = mydb.connect(
        host = "localhost",
        port = "3306",
        user = "user",
        password = "pass",
        database = "toshokan"
        )

    cur = conn.cursor()
    
    while True:
            
        b_id = input("図書IDを入力してください。　（00　終了） \n> ")
        try:
            b_id = int(b_id)
    
        except ValueError:
            print("数字で入力してください。")
            continue
        except Exception:
            print("エラーが発生しました。")
    
        if b_id == 00:
            print("終了しました。")
            break 
    
        else:
            # 削除したい図書情報を表示させる
            cur.execute("SELECT * from books where b_id = %s", (b_id,))
            row = cur.fetchall()
            p_date = str(row[0][5])

            print("=" * 20)
            print(f"<isbn>    {row[0][1]}")
            print(f"<図書名>  {row[0][2]}")
            print(f"<著者名>  {row[0][3]}")
            print(f"<出版社>  {row[0][4]}")
            print(f"<出版日>  {p_date.replace('-','/')}")
            print("=" * 20)
        
    
        # 削除済みのデータだった場合
        if row[0][7] == 0:
            print("この図書は既に削除されています。")

        else:   
            inp = input("この図書を削除しますか？ (はい:yes | いいえ:no)\n> ")
            
        
        if inp == "yes":
    
            # 貸出可の図書を削除登録する（statusとd_flagを更新）
            if row[0][6] == 1:
                       
                # ｓｔａｔｕｓを0にする
                cur.execute("UPDATE books set status = status -1 where b_id = %s",(b_id,))
                # d_flagを0にする
                cur.execute("UPDATE books set d_flag = d_flag -1 where b_id = %s",(b_id,))
                        
                print(f"図書{row[0][2]}を削除しました。")
                conn.commit()
                    
            # 貸出中の図書の場合は削除不可
            else:
                print("貸出中の図書を削除できません。")
            
        # noを入力した時は登録処理は中止する
        else:
            print("削除登録を中止しました。")
                        
    cur.close()
    conn.close()


deleteBook()

