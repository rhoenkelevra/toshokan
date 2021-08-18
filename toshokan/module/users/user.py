# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 10:47:10 2021

@author: user24
"""
from module.setup.connect import connect
from getpass import getpass


class User:

    def __init__(self):
        self.login = 0
        self.loginName = ""
        

    def login_user(self):
        con = connect()
        cursor = con.cursor()
        
        success = False
        print("\n" + "-" * 7, "ログイン", "-" * 7)
        while success == False:
            try:
                u_id = int(input("ユーザIDを入力 \n>"))
            except:
                print("ログインIDまたはパスワードが違います。")
                continue
            u_pass = getpass("パスワードを入力 \n>")
            
            data = (u_id, u_pass)
            cursor.execute("SELECT u_id, u_name, d_flag FROM users where u_id=%s and u_pass=%s ", data)
            
            rows = cursor.fetchall()
            
            if cursor.rowcount == 1:
            #ｄｆｌａｇ確認
                if rows[0][2] == 0:
                    print("ユーザがありません。")
                    continue
            else:
                print("ログインIDまたはパスワードが違います。")
                continue
                
            self.login = rows[0][0]
            self.loginName = rows[0][1]
            
            
            success = True
            
        print("\n")
        print(f"ようこそ {self.loginName} さん。")
        cursor.close()
        con.close()
        return success

    def logout(self):
        self.login = 0
        print("ログアウトしました。")

    def add_user(self):
        con = connect()
        cursor = con.cursor(buffered=True)
        
        u_name = input("ユーザの名前を入力してください。（00　終了） \n>")
        
        user_created = False
        # ｐａｓｓを正しく入れるまで
        while user_created == False:
            u_pass = input("パスワードを入力してください。\n>")
            while len(u_pass) < 4 or len(u_pass) > 8:
                u_pass = input("パスワードは半角英数字で最小4文字、最大8文字で入れてください。\n>")
            
                
            u_pass2 = input("確認の為パスワードもう一度入力してください。\n>")
            if u_pass != u_pass2:
                print("パスワードが合わない。最初からもう一度入力してください。")
                continue
                
            user_created = True
       
        data = (u_name, u_pass)

        cursor.execute("insert into users (u_name, u_pass) values (%s, %s)", data)
        con.commit()
        print("登録しました。")
        cursor.close()
        con.close()
    
    def delete_user(self):
        con = connect()
        cursor = con.cursor(buffered=True)
        
        deleteStatus = False
        while deleteStatus == False:
            try:
                u_id = int(input("ユーザのIDを入力してください。（00　終了） \n>"))
            except:
                print("数値を入れてください。")
                continue
            
            if u_id == 00:
                break
            
            cursor.execute("select u_id, u_name from users where u_id=%s", (u_id,))
            res = cursor.fetchall()
            if cursor.rowcount == 0:
                print("ユーザを見つかりませんでした。")
                continue
            for row in res:
                print("=" * 10)
                print(f"ユーザＩＤ： {row[0]}")
                print(f"ユーザ名：　{row[1]}")
                print("=" * 10)
                
            
            confirm = input("この内容で削除して良いですか？\n（はい：y / いいえ：n)\n>")
            
            if confirm == "n":
                continue
            
            if confirm == "y":
                cursor.execute("update users set d_flag=0 where u_id=%s", (u_id,))  
                print("削除できました。")
                deleteStatus = True
                con.commit()
                cursor.close()
                con.close()
                
                
    def show_user(self):
        con = connect()
        cursor = con.cursor(buffered=True)
        
        cursor.execute("select u_id, u_name, d_flag from users GROUP BY d_flag ORDER BY u_id")
        
        res = cursor.fetchall()
        
        for row in res:
            print("=" * 10)
            print(f"ユーザＩＤ：　{row[0]}")
            print(f"ユーザ名：　{row[1]}")
            
            if row[2] == 0:
                print("状態：　削除済み")
                status = "sakujo"
            else:
                status = "active"
                print(f"状態：　{status}")
                
            print("=" * 10)
            
        
        
# =============================================================================
# オプション　ＣＳＶ出力

#         export = input("Export?")
#         print(res)
#         res_list = list(res)
#         if export == "y":
#             with open('test.csv', 'w', encoding='UTF8') as f:
#                 writer = csv.writer(f)
#                 for row in res_list:
#                     row_list = list(row)
#                     print(row_list)
#                     if row_list[2] == 0:
#                         row_list[2] = "Deleted"
#                     else:
#                         row_list[2] = "Active"   
#                         
#                     # writer.writerow([row_list[0], row_list[1], row_list[2]] )
#                     writer.writerow(row_list)
# =============================================================================
                
     
# user = User()
# user.delete_user()
