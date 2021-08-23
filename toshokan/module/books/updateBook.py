from module.setup.connect import connect
import re
from datetime import datetime
from datetime import timedelta


def ShowBookData(row):

    print("=" * 60)
    print("図書ID:".ljust(9) + str(row[0][0]))
    print("isbn:".ljust(11) + str(row[0][1]))
    print("図書名:".ljust(8) + str(row[0][2]))
    print("著者名:".ljust(8) + str(row[0][3]))
    print("出版社:".ljust(8) + str(row[0][4]))
    print("出版日:".ljust(8) + str(row[0][5]).replace("-", "/"))
    print("=" * 60)


def updateBook():

    try:

        # コネクションの作成
        conn = connect()
        cur = conn.cursor()

        while True:

            try:
                b_id = int(input("図書IDを入力してください。　（00　終了） \n> "))

            except ValueError:
                print("数字で入力してください。")
                continue

            if b_id == 00:
                break

            else:
                # 変更・更新したい図書の情報を表示する
                cur.execute("SELECT * from books where b_id = %s", (b_id,))
                row = cur.fetchall()

                # 削除済みの図書は変更できない
                if row[0][7] == 0:
                    print("この図書は既に削除されています。")

                else:
                    # 図書情報を表示させる
                    ShowBookData(row)

                    inp = input("この図書情報を変更しますか？ (はい:y / いいえ:n)\n> ")

                    if inp == "y":

                        # 貸出可の図書かどうか
                        if row[0][6] == 1:

                            while True:
                                print("\n変更する項目の番号を入力ください。")
                                inp = input(
                                    "1: isbn\n2: 図書名\n3: 著者名\n4: 出版社名\n5: 出版日\n> "
                                )

                                if inp == "":
                                    print("入力されていません。")
                                    continue

                            # 1: isbn の変更
                            if inp == 1:
                                while True:
                                    inp_isbn = input("変更内容を入力してください。\n>")
                                    if inp_isbn == "":
                                        print("isbnが入力されていません。")
                                        continue
                                    break

                                data = (inp_isbn, b_id)
                                cur.execute(
                                    "UPDATE books set isbn = %s where b_id = %s",
                                    data,
                                )

                            # 2: 図書名の変更
                            elif inp == 2:
                                inp_title = input("変更内容を入力してください。(40字以内)\n>")
                                while True:
                                    if inp_title == "":
                                        print("図書名が入力されていません。")
                                        inp_title = input(
                                            "図書名を入力してください(40字以内)。\n>"
                                        )

                                    elif len(inp_title) > 40:
                                        print("図書名の長さが最大値を超えています。")
                                        inp_title = input(
                                            "図書名を入力してください(40字以内)。\n>"
                                        )
                                    break

                                data = (inp_title, b_id)
                                cur.execute(
                                    "UPDATE books SET title = %s where b_id = %s",
                                    data,
                                )
                                row = cur.fetchone()

                            # 3: 著者名の変更
                            elif inp == 3:
                                while True:
                                    inp_data = input("変更内容を入力してください。\n>")
                                    if inp_data == "":
                                        print("著者名が入力されていません。")
                                        continue
                                    break

                                data = (inp_data, b_id)
                                cur.execute(
                                    "UPDATE books set author = %s where b_id = %s",
                                    data,
                                )
                                row = cur.fetchone()

                            # 　4: 出版社名の変更
                            elif inp == 4:
                                while True:
                                    inp_data = input("変更内容を入力してください。\n>")
                                    if inp_data == "":
                                        print("出版社名が入力されていません。")
                                        continue
                                    break
                                data = (inp_data, b_id)
                                cur.execute(
                                    "UPDATE books set p_name = %s where b_id = %s",
                                    data,
                                )
                                row = cur.fetchone()

                            # 　5: 出版日の変更
                            elif inp == 5:
                                date_insert = False
                                while date_insert == False:

                                    inp_p_date = input(
                                        "変更内容を入力してください。(YYYY / MM / DD )\n>"
                                    )

                                    date_format = re.search(
                                        "\d\d\d\d[/]\d\d[/]\d\d", inp_p_date
                                    )
                                    if not date_format:
                                        print(
                                            "入力できる日付は、数字および ”/” のみです。（例：2000/10/12）"
                                        )
                                        continue

                                    try:
                                        inp_p_date_obj = datetime.strptime(
                                            inp_p_date, "%Y/%m/%d"
                                        ).date()
                                        in_limit_date = (
                                            inp_p_date_obj + timedelta(days=5)
                                        )
                                        in_limit_date_str = str(in_limit_date)
                                        in_limit_date_str = (
                                            in_limit_date_str.replace("-", "/")
                                        )
                                    except:
                                        print(
                                            "入力できる日付の範囲は1/01/01～9999/12/31にしてください。"
                                        )
                                        continue

                                    date_insert = True

                                data = (inp_p_date, b_id)
                                cur.execute(
                                    "UPDATE books set p_date = %s where b_id = %s",
                                    data,
                                )
                                row = cur.fetchone()

                            else:
                                # print("削除登録を中止しました。")
                                continue

                                # この内容でよろしいですか？　(y/n)
                                inp = input(
                                    "この変更内容でよろしいですか？ (はい:y / いいえ:n)\n> "
                                )
                                if inp == "y":

                                    # SQLに登録完了
                                    conn.commit()
                                    cur.execute(
                                        "SELECT * from books where b_id = %s",
                                        (b_id,),
                                    )
                                    row = cur.fetchall()
                                    print("変更しました。")

                                    ShowBookData(row)

                                else:
                                    print("変更登録を中止しました.")
                                break

                        # 貸出中の図書の場合は削除不可
                        else:
                            print("貸出中の図書は変更できません。")

                    # noを入力した時は登録処理は中止する
                    else:
                        print("変更登録を中止しました。")

    except:
        print("エラーになりました。")

    finally:

        cur.close()
        conn.close()


# updateBook()
