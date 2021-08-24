# -*- coding: utf-8 -*-
from module.setup.connect import connect
from getpass import getpass
import unicodedata


class User:
    def __init__(self):
        self.login = 0
        self.loginName = ""
        self.login_status = False
        self.__admin = 1000

    def get_admin(self):
        return self.__admin

    # ================== 管理者ログイン ===================
    def login_user(self):
        try:
            conn = connect()
            cur = conn.cursor()

            success = False
            print("\n" + "-" * 7, "ログイン", "-" * 7)
            while success == False:
                try:
                    u_id = int(input("ログインIDを入力 \n>"))
                except:
                    print("ログインIDまたはパスワードが違います。")
                    continue
                u_pass = getpass("パスワードを入力 \n>")

                data = (u_id, u_pass)
                cur.execute(
                    "SELECT u_id, u_name, d_flag FROM users where u_id=%s and u_pass=%s ",
                    data,
                )

                rows = cur.fetchall()

                if cur.rowcount == 1:
                    # ｄｆｌａｇ確認
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
            print(f"ようこそ　{self.loginName}さん")
            self.login_status = True
            return self.login_status

        except Exception as error:
            print(error)
        finally:
            cur.close()
            conn.close()

    # ================== 管理者ログアウト =================
    def logout(self):
        self.login = 0
        print("ログアウトしました。")

    # ================== 管理者登録 ===================
    def add_user(self):
        # TODO don't accept empty name
        # TODO don't accept symbols
        try:
            conn = connect()
            cur = conn.cursor(buffered=True)

#TODO [x]check for empty in username
#TODO [x]check for symbols in password
            user_name_input = False
            while user_name_input == False:
                u_name = input("ユーザ名を入力してください。（00　終了） \n>")
                if u_name == "":
                    print("ユーザ名が入力されていません。")
                    continue

                user_name_input = True

            if u_name == "00":
                return
            user_created = False
            # ｐａｓｓを正しく入れるまで
            while user_created == False:
                check = False
                while check == False:
                    u_pass = input("パスワードは半角英数字で最小4文字、最大8文字で入力してください。\n>")

                    letter_cnt = 0
                    for c in u_pass:
                        letter = unicodedata.east_asian_width(c)
                        # Na=半角英数
                        if letter != "Na":
                            letter_cnt += 1
                        if c.isalnum() == False:
                            letter_cnt += 1
                            print(c, letter_cnt)

                    if (
                        len(str(u_pass)) < 4
                        or len(str(u_pass)) > 8
                        or letter_cnt >= 1
                    ):

                        continue

                    # パス確認
                    u_pass2 = input("確認の為パスワードもう一度入力してください。\n>")

                    if u_pass != u_pass2:
                        print("パスワードが合わない。最初からもう一度入力してください。")
                        continue

                    # パス確認
                    check = True

                user_created = True

            data = (u_name, u_pass)

            cur.execute(
                "insert into users (u_name, u_pass) values (%s, %s)", data
            )
            conn.commit()
            new_id = cur.lastrowid

            print("=" * 30)
            print(f"名前：　　　　{u_name}")
            print(f"ログインID：　{new_id}")
            print(f"パスワード：　{u_pass}")
            print("=" * 30)
            print("登録しました。")

        except Exception as error:
            print(error)
        finally:
            cur.close()
            conn.close()

    # ================== 管理者削除 ===================
    def delete_user(self):
        try:
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

                cur.execute(
                    "select u_id, u_name from users where u_id=%s", (u_id,)
                )
                res = cur.fetchall()
                if cur.rowcount == 0:
                    print("ユーザを見つかりませんでした。")
                    continue
                for row in res:
                    print("=" * 30)
                    print(f"ユーザID：  {row[0]}")
                    print(f"ユーザ名：　{row[1]}")
                    print("=" * 30)

                confirm = input("この内容で削除して良いですか？ （はい：y / いいえ：n)\n>")

                if confirm == "n":
                    continue

                if confirm == "y":
                    cur.execute(
                        "update users set d_flag=0 where u_id=%s", (u_id,)
                    )
                    print("削除できました。")
                    deleteStatus = True
                    conn.commit()

        except Exception as error:
            print(error)
        finally:
            cur.close()
            conn.close()

    # ================== 管理者一覧 ===================
    def show_users(self):
        try:
            conn = connect()
            cur = conn.cursor(buffered=True)

            cur.execute(
                "select u_id, u_name, d_flag from users where d_flag=1 ORDER BY u_id"
            )

            res = cur.fetchall()

            for row in res:
                print("=" * 30)
                print(f"ユーザID：　{row[0]}")
                print(f"ユーザ名：　{row[1]}")
                print("=" * 30)

        except Exception as error:
            print(error)

        finally:
            cur.close()
            conn.close()


# user = User()
# user.add_user()
