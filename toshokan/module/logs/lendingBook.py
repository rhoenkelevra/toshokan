import re
from datetime import datetime
from datetime import timedelta

from module.setup.connect import connect  

# 各テーブルより呼出照合テスト関数
def idtest(table_name,id_type,id):
    con = connect()
    cur = con.cursor()
    table = table_name
    ids = id_type
   
    cur.execute(f"select*from {table} where {ids}= %s", (id,))   
    results = cur.fetchall()
    
    # 照合がない場合
    if cur.rowcount < 0:               
        if table_name == "books":
            print("不正な図書IDが入力されました。")    
        if table_name == "customer":
            print("不正な利用者IDが入力されました。")           
        success = False
        return success
   
    success = True
    for row in results:
        print(row)        
    return success

# 図書貸出の関数
def lendingBook():
    conn = connect()
    cur = conn.cursor(buffered=True)
    
    condition = True
    while condition == True:

        # 図書の選択
        success = False
        while success == False:
            
            try:
                b_id = int(input("図書IDを選択してください。(00で終了）\n>"))
                
                if b_id == 00:
                    break
                success = idtest("books", "b_id", b_id)
                
            except:
                print("不正な図書IDが入力されました。")
                continue
            
 
# =================================================================
        # ユーザーIDの選択 ※自動でログイン時のIDにする
        try:
            u_id = int(input("ユーザーIDを入力してください。(00で終了）\n>"))
            
            if u_id == 00:
                break
            
        except:
            print("数値を入力してください。")
            continue 
# =================================================================

        
        # 利用者IDの選択 
        success = False
        while success == False:
            try:
                c_id = int(input("利用者IDを入力してください。(00で終了）\n>"))
                
                if c_id == 00:
                    break
                
            except:
                print("不正な利用者IDが入力されました。")
                continue
            
            success = idtest("customer", "c_id", c_id)
        
        # 貸出日の入力
        date_insert = True
        while date_insert == True:
            out_date = input("貸出日（YYYY/MM/DD）を入力してください。\n>")
            
            
            date_format = re.search("\d\d\d\d[/]\d\d[/]\d\d",out_date )
        
            if not date_format:
                print("入力できる日付は、数字および”/”のみです。(例:2000/10/12)")
                continue
            
            date_insert = False
            
            
        # date型に変換
        out_date_obj = datetime.strptime(out_date,"%Y/%m/%d").date()
        in_limit_date = out_date_obj + timedelta(days=5)  
        in_limit_date_str = str(in_limit_date)
        in_limit_date_str = in_limit_date_str.replace("-", "/")
  
        # メモの入力     
        memo = input("メモを入力してください。\n>") 
 
        
        # 入力内容確認 
        print("="*50)
        print("図書D:",b_id)
        print("ユーザーID:",u_id)
        print("利用者ID:",ｃ_id)
        print("貸出日:",out_date)
        print("メモ:",memo)      
        
        inp = input("この内容で登録してよろしいですか？( はい：y / いいえ：n )\n>")
        
        if inp == "n":
            break
        
        if inp == "y":

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
        data = (u_id, b_id, c_id, out_date, in_limit_date, memo )
        cur.execute("insert into log (u_id, b_id, c_id, out_date, in_limit_date, memo ) values(%s, %s, %s, %s, %s, %s)", data)
        print(cur.rowcount,"件、登録しました。")
        
        cur.execute("select title from books where b_id = %s", (b_id,))
        title = cur.fetchall()
        
        cur.execute("select c_name from customer where c_id = %s", (c_id,))
        c_name = cur.fetchall()

        # 登録した図書情報の表示
        print("=" * 50)
        print("図書ID:",b_id)
        print("図書名:",title[0][0])
        print("利用者ID:",ｃ_id)
        print("利用者名:",c_name[0][0])       
        print("貸出日:",out_date)
        print("貸出期限:",in_limit_date_str)
        print("=" * 50)          
 
        # 更新の確定         
        conn.commit()    
    
    # while文を抜ける
    condition = False  

    # カーソル、コネクションの切断
    cur.close()
    conn.close()

# =============================================================================
# # 共有→　ｃチーム　ファイル管理　完成ファイルに入れる際、「lendingBook()」削除
# # 図書貸出の関数の実行         
lendingBook()        
# =============================================================================
