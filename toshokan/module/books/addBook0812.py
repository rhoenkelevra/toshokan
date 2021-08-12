import re

def addBook():
    
    import mysql.connector as mydb

    # コネクションの作成
    conn = mydb.connect(
        host = "localhost",
        port = "3306",
        user = "root",
        password = "pass",
        database = "toshokan"
    ) 

    # カーソルの作成
    cur = conn.cursor()    
        
    # 図書登録
    while True:
        try:
            check = 2
            isbn = int(input("isbnを入力してください。　（00　終了） \n>"))

            # 図書登録の終了
            if isbn ==00:
                print("図書登録を終了しました。")
                break

            cur.execute("select * from books where isbn = %s", (isbn,))
            cur.fetchall()
                  
            # 図書登録の判定
            if cur.rowcount > 0:
                # 登録済み図書の場合（登録処理を行わない）
                print("登録済みの図書です。")
                continue
            else:
                # 未登録図書の場合
                title = input("図書名を入力してください(40字以内)。\n>")
                
                while title == "":
                    print("図書名が入力されていません。")
                    title = input("図書名を入力してください(40字以内)。\n>")
              
                while len(title) > 40:
                    print("図書名の長さが最大値を超えています。")
                    title = input("図書名を入力してください(40字以内)。\n>")                
                
                
                author = input("著者名を入力してください。\n>")
                p_name = input("出版社を入力してください。\n>")
                p_date = input("出版日(YYYY / MM / DD )を入力してください。\n>")
                
                #TODO 
                # date_format = re.search('\d\d\d\d[/]\d\d[/]\d\d', p_date)
                # while not date_format:
                #     if not date_format:
                #         print('入力できる日付は、数字および ”/” のみです。（例：2000/10/12）') 
                #         p_date = input("出版日(YYYY / MM / DD )を入力してください。\n>")
                #         continue
          
                # 入力情報の表示
                print("=" * 50)
                print(f"isbn：    {isbn}")
                print(f"図書名：  {title}")
                print(f"著者名：  {author}")
                print(f"出版社：  {p_name}")
                print(f"出版日：  {p_date}")                
                print("=" * 50)

    
                # 登録内容に誤りがあるかを確認                
                check = input("この内容で登録して良いですか？（はい：y / いいえ：n）\n>")
                if check == "y":
                    # 図書をbooksテーブルへ追加
                    # statusとd_flagは初期値として1を入力する
                    books = (isbn, title, author, p_name, p_date, 1, 1)
                    cur.execute(
                        "insert into books (isbn, title, author, p_name, p_date, status, d_flag) values(%s, %s, %s, %s, %s, %s, %s)", books)
                
                    # 追加失敗の時はエラーにする
                    if cur.rowcount == 0:
                        raise Exception
          
                    # 更新を確定する
                    conn.commit()
                    cur.execute(
                        "select * from books where isbn = %s", (isbn,))
                    row = cur.fetchall()              
                
                    # 登録した図書情報の表示
                    print("図書を登録しました。")
                    print("=" * 50)
                    print(f"図書ID：  {row[0][0]}")
                    print(f"isbn：    {row[0][1]}")
                    print(f"図書名：  {row[0][2]}")
                    print(f"著者名：  {row[0][3]}")
                    print(f"出版社：  {row[0][4]}")
                    print(f"出版日：  {row[0][5]}")
                    print("=" * 50)

                else:                                       
                    print("図書登録を中止しました。")
                    continue                    

        # 追加失敗時は全て取りやめ
        except:
            # conn.rollback()     # 無くても良いかも
            print("図書登録に失敗しました。")
              
    # カーソルの切断
    cur.close()
    # コネクションの切断
    conn.close()


# =============================================================================
# 実行 
# =============================================================================
# addBook()

