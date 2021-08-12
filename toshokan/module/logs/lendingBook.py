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

# 各テーブルとIDの照合
def idtest(table_name,id_type,id):
    con = connect()
    cur = con.cursor(buffered=True)
    table = table_name
    ids = id_type
    cur.execute(f"select * from {table} where {ids}=%s", (id,))
    res = cur.fetchone()
    if cur.rowcount == 0:
        if table == "books":
            print("不正な図書IDが入力されました。")
        if table == "customer":
            print("不正な利用者IDが入力されました。")
        if table == "customer":
            print("不正な利用者IDが入力されました。")
        success = False
        return success
    
    print(res)
    success = True
    return success

# 図書の貸出を登録
def lendingBook():
    con = connect()
    cur = con.cursor(buffered=True)
    
    condition = True
    while condition == True:

    # 図書の選択
        try:
            b_id = int(input("図書IDを選択してください。"))
        except:
            print("数値を入力してください。")
            continue
            
        success = idtest("books", "b_id", b_id)
        if success == False:
            continue
    

    # ユーザーIDの選択
        try:
            u_id = input("ユーザーIDを入力してください。")
        except:
            print("数値を入力してください。")
            continue
        success = idtest("users", "u_id", u_id)
        if success == False:
            continue
        
        
        
    # 利用者IDの選択   
        try:
            c_id = int(input("カスタマーIDを入力してください。"))
        except:
            print("数値を入力してください。")
            continue
        success = idtest("customer", "c_id", c_id)
        if success == False:
            continue
        
    # 貸出日の入力     
        out_date = input("貸出日（yyyy/mm/dd）を入力してください。")
  
    # メモの入力     
        memo = input("メモを入力してください。")
        # 変数へ代入し、logテーブルへデータ挿入
        data = (u_id, b_id, c_id, out_date, memo )
        cur.execute("insert into log (u_id, b_id, c_id, out_date, memo ) values(%s, %s, %s, %s, %s)", data)
        print(cur.rowcount,"件、登録しました。")
        
        condition = False
       
   
    con.commit()
    cur.close()

    con.close()
          
# TODO
# =============================================================================
#     inp = input("利用者IDを入力してください。")
#     
#     
#     log  = []
#     
#     
#    
#     cur.close()
#     con.close()    
#     cur.execute()
#             
# =============================================================================
lendingBook()        



