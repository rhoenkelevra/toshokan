# -*- coding: utf-8 -*-
#!/usr/bin/env python

from module.users.user import User

from module.logs.returnBook import returnBook
from module.logs.lendingBook import lendingBook

from module.books.addBook import addBook
from module.books.deleteBook import deleteBook
from module.books.showBook import showBook
from module.books.updateBook import updateBook

from module.books.csvBook import csvBook
from module.books.csvBook_lending import csvBook_lending

from module.customers.addCustomer import addCustomer
from module.customers.deleteCustomer import deleteCustomer
from module.customers.showCustomer import showCustomer
from module.customers.csvCustomer import csvCustomer
from module.customers.updateCustomer import updateCustomer

from module.option.optentai import optentai
from module.option.optninki import optninki


def main():
    print("\n")
    print("-" * 3, "アプリケーションへようこそ", "-" * 7)
    print("-" * 3,"図書貸出システム  Provided by Cube")
    # ===========================================================
    #                       ログイン
    # ===========================================================
    user = User()

    while True:
        # ログイン状態の有無で出力内容変更
        if user.login == 0:
            print("\n")
            print("-" * 6, "トップメニュー", "-" * 17)

            try:
                inp = int(input("1:ログイン　00:終了 \n>"))
            except:
                print("数値を入れてください。")
                continue

        # 00と入力されたらプログラム終了
        if inp == 00:
            break
        if inp == 1:
            if user.login == 0:
                # ログイン関数を呼び出す、ＩＤとＰＡＳＳ確認してＯＫだとsuccess=True
                user.login_user()

        # ======================================================
        #                       メニュー
        # ======================================================
        if user.login_status is True:

            print("=" * 10, "メニュー", "=" * 10)

            # ============================ 全員用メニュー ====================
            if user.login != user.get_admin():
                try:
                    menu_choice = int(
                        input(
                            "1: 図書貸出\n2: 図書返却\n3: 図書管理\n4: 利用者管理\n5: オプション\n9: ログアウト \n>"
                        )
                    )
                except:
                    print("数値を入れてください。")
                    continue

                # ============================ ログアウト  =========================
                if menu_choice == 9:
                    user.logout()

                # ============================ 貸出・返却  =======================
                if menu_choice == 1:
                    lendingBook(user.login)
                if menu_choice == 2:
                    returnBook()

                # ============================ 図書管理 =========================
                if menu_choice == 3:

                    try:
                        book_menu = int(
                            input(
                                "1: 図書登録\n2: 図書削除\n3: 図書一覧\n4: 図書CSV出力\n5: 貸出中図書CSV出力\n00: 戻る\n>"
                            )
                        )
                    except:
                        print("数値を入れてください。")
                        continue

                    if book_menu == 00:
                        continue

                    if book_menu == 1:
                        addBook()
                    if book_menu == 2:
                        deleteBook()
                    if book_menu == 3:
                        showBook()
                    if book_menu == 4:
                        csvBook()
                    if book_menu == 5:
                        csvBook_lending()
                    if book_menu == 6:
                        updateBook()

# ============================ 利用者管理  ===================
                if menu_choice == 4:
                    try:
                        customer_menu = int(
                            input(
                                "1: 利用者登録\n2: 利用者削除　\n3: 利用者一覧\n4: 利用者CSV出力\n00: 戻る\n>"
                            )
                        )
                    except:
                        print("数値を入れてください。")
                        continue

                    if customer_menu == 00:
                        continue

                    if customer_menu == 1:
                        addCustomer()
                    if customer_menu == 2:
                        deleteCustomer()
                    if customer_menu == 3:
                        showCustomer()
                    if customer_menu == 4:
                        csvCustomer()
                        
                if menu_choice == 5:
                    option_menu = int(input("1: 延滞書名リスト\n2: 人気図書リスト\n3: 図書更新\n4: 利用者更新\n00: 戻る\n>"))
            
                    if option_menu == 00:
                        continue
                    
                    if option_menu == 1:
                        optentai()
                        
                    if option_menu == 2:
                        optninki()
                        
                    if option_menu == 3:
                        updateBook()
                        
                    if option_menu == 4:
                        updateCustomer()

            # ===========================================================
            #                           ユーザ用
            # ===========================================================
            
            if user.login == user.get_admin():
                try:
                    kanri_menu = int(
                        input("1: ユーザ登録\n2: ユーザ削除\n3: ユーザ一覧\n9: ログアウト\n>")
                    )

                except:
                    print("数値を入れてください。")
                    continue

                if kanri_menu == 1:
                    user.add_user()

                if kanri_menu == 2:
                    user.delete_user()

                if kanri_menu == 3:
                    user.show_users()

                if kanri_menu == 9:
                    user.logout()


main()
