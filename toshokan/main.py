# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 14:34:58 2021

@author: user24
"""
from module.logs.returnBook import returnBook
from module.login.login import Login
from module.books.addBook0812 import addBook


print("-" * 7, "アプリケーションへようこそ", "-" * 7)
# =============================================================================
#   ログイン
# =============================================================================
user = Login()
while True:
    # ログイン状態の有無で出力内容変更
    if user.login == 0:
        print("\n" + "-" * 7, "トップメニュー", "-" * 7)

        inp = int(input("1:ログイン　2:新規ユーザ登録　00:終了 \n>"))
    # 00と入力されたらプログラム終了
    if inp == 00:
        break
    if inp == 1:
        if user.login == 0:
            print("\n" + "-" * 7, "ログイン", "-" * 7)
            try:
                u_id = int(input("ユーザIDを入力 \n>"))
            except:
                print("ログインIDまたはパスワードが違います。")
                continue
            u_pass = input("パスワードを入力 \n>")
            success = user.login_user(u_id, u_pass)

    # =============================================================================
    #   メニュー
    # =============================================================================
    if success is True:
        print("\n\n")
        print("=" * 10, "メニュー", "=" * 10)
        menu_choice = int(
            input("①・図書貸出　②・図書返却　③・図書管理　④・利用者管理　⑤・管理者用　⑨・ログアウト \n>")
        )

        if menu_choice == 1:
            pass
        if menu_choice == 2:
            returnBook()

        if menu_choice == 3:
            addBook()
        if menu_choice == 4:
            pass
        if menu_choice == 5:
            pass
        if menu_choice == 9:
            user.logout()
