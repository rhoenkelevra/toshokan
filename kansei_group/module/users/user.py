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
        self.login_status = False
        

    def login_user(self):
        conn = connect()
        cur = conn.cursor()
        
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
            cur.execute("SELECT u_id, u_name, d_flag FROM users where u_id=%s and u_pass=%s ", data)
            
            rows = cur.fetchall()
            
            if cur.rowcount == 1:
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
        self.login_status = True
        cur.close()
        conn.close()
        return self.login_status

    def logout(self):
        self.login = 0
        print("ログアウトしました。")

    def add_user(self):
        conn = connect()
        cur = conn.cursor(buffered=True)
        
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

        cur.execute("insert into users (u_name, u_pass) values (%s, %s)", data)
        conn.commit()
        new_id = cur.lastrowid
        
        
        print("=" * 30)
        print(f"ユーザ名：　{u_name}")
        print(f"ユーザＩＤ：　{new_id}")
        print(f"パスワード：　{u_pass}")
        print("登録しました。")
        print("=" * 30)
        
        cur.close()
        conn.close()
    
    def delete_user(self):
        conn = connect()
        cur = conn.cursor(buffered=True)
        
        deleteStatus = False
        while deleteStatus == False:
            try:
                u_id = int(input("ユーザのIDを入力してください。（00　終了） \n>"))
            except:
                print("数値を入れてください。")
                continue
            
            if u_id == 00:
                break
            
            cur.execute("select u_id, u_name from users where u_id=%s", (u_id,))
            res = cur.fetchall()
            if cur.rowcount == 0:
                print("ユーザを見つかりませんでした。")
                continue
            for row in res:
                print("=" * 30)
                print(f"ユーザＩＤ： {row[0]}")
                print(f"ユーザ名：　{row[1]}")
                print("=" * 30)
                
            
            confirm = input("この内容で削除して良いですか？\n（はい：y / いいえ：n)\n>")
            
            if confirm == "n":
                continue
            
            if confirm == "y":
                cur.execute("update users set d_flag=0 where u_id=%s", (u_id,))  
                print("削除できました。")
                deleteStatus = True
                conn.commit()
                cur.close()
                conn.close()
                
                
    def show_users(self):
        conn = connect()
        cur = conn.cursor(buffered=True)
        
        cur.execute("select u_id, u_name, d_flag from users where d_flag=1 ORDER BY u_id")
        
        res = cur.fetchall()
        
        for row in res:
            print("=" * 30)
            print(f"ユーザＩＤ：　{row[0]}")
            print(f"ユーザ名：　{row[1]}")
            print("=" * 30)
            
        cur.close()
        conn.close()
        

     
# user = User()
# user.login_user()
