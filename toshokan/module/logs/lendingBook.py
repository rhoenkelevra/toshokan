import mysql.connector as mydb
def connect():
    conn = mydb.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    password = "pass",
    database = "toshokan"
) 
    return conn

# ======================================================================
# 各テーブルより呼出照合テスト関数
# def idtest(table_name,id_type,id):
#     con = connect()
#     cur = con.cursor()
#     sql = "select*from {table_name} where {id_type}= %s"
#     sql.format(table_name, id_type)
#     cur.execute(sql (id,))    
#     # 照合がない場合
#     if cur.rowcount < 0:               
#         if table_name == "books":
#             print("不正な図書IDが入力されました。")    
#         if table_name == "customer":
#             print("不正な利用者IDが入力されました。")           
#         success = False
#         return success
#     results = cur.fetchall()
#     count = cur.rowcount
#     print(count)
#     success = True
#     for row in results:
#         print(row)        
#     return success
# ======================================================================

# 図書貸出の関数
def lendingBook():
    con = connect()
    cur = con.cursor(buffered=True)
    
    condition = True
    while condition == True:

    # 図書の選択
        try:
            b_id = int(input("図書IDを選択してください。"))
        except:
            print("不正な図書IDが入力されました。")
            continue
            
    # ユーザーIDの選択 ※自動でログイン時のIDにする
        try:
            u_id = int(input("ユーザーIDを入力してください。"))
        except:
            print("数値を入力してください。")
            continue 
        
    # 利用者IDの選択 
        try:
            c_id = int(input("利用者IDを入力してください。"))
        except:
            print("不正な利用者IDが入力されました。")
            continue
        
    # 貸出日の入力     
        out_date = input("貸出日（yyyy/mm/dd）を入力してください。")
  
    # メモの入力     
        memo = input("メモを入力してください。") 


        # d_flag確認
        cur.execute("select d_flag, b_id from books where b_id = %s ", (b_id,))
        rows = cur.fetchone()  
        
        if rows[0] == 0:
            print("図書は削除されています。")
            continue  

        # status +1
        cur.execute("select status, b_id from books where b_id = %s ", (b_id, ))
        rows = cur.fetchone()  
        
        if rows[0] == 1 :
             cur.execute("update books set status = status - 1 where b_id = %s",(b_id,))

        else:
            print("図書はすでに貸出中です。")
            continue  
    
        # qtybook +1
        cur.execute("select qtybooks, c_id from customer where c_id =%s ", (c_id,))
        rows = cur.fetchone()  
        
        if rows[0] < 3:
             cur.execute("update customer set qtybooks = qtybooks + 1 where c_id = %s",(c_id,))

        else:
            print("利用者はすでに3冊の図書を借りています。")
            continue


        
    # 変数へ代入し、logテーブルへデータ挿入
        data = (u_id, b_id, c_id, out_date, memo )
        cur.execute("insert into log (u_id, b_id, c_id, out_date, memo ) values(%s, %s, %s, %s, %s)", data)
        print(cur.rowcount,"件、登録しました。")          
 
    # 更新の確定         
        con.commit()    
    
    # while文を抜ける
    condition = False  

    # カーソル、コネクションの切断
    cur.close()
    con.close()

# 図書貸出の関数の実行         
lendingBook()        
