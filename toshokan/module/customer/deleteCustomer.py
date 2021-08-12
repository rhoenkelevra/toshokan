# def deleteCustomer():


# 機能　利用者の削除 deleteCustomer

# 接続
import mysql.connector as mydb

conn = mydb.connect(
    host="localhost", port="3306", user="user", password="pass", database="toshokan"
)

cur = conn.cursor()

print("利用者の削除を行います")
print(" " * 50)
# 利用者一覧表示(削除されたデータ以外表示)
cur.execute("select c_name,c_id from customer where d_flag = 1 order by c_name")
"""
#削除する利用者を選択（利用者名検索　）
dname = input ("削除する利用者名を入れてください")

#利用者・id表示

cur.execute("select * from customer where c_name =%s,dname")
#cur.execute("select * from customer where c_name like '"+%s(dname)+"'")
#cur.execute("select * from customer where c_name like sara%")
"""

print("登録利用者名とIDの一覧を表示します　（削除する利用者のIDを選択してください")
print(" " * 50)

rows = cur.fetchall()
for row in rows:
    (rname, rid) = row
    print(f"利用者名:　{rname},　　　利用者ID: {rid} ")

# 削除を選択する　（削除するidを入力）

did = (input("選択した削除するIDを入力してください"),)
# print(did)

# 利用者削除確認へ遷移
# 選択したidで利用者の情報確認

cur.execute("select * from customer where c_id = %s", did)
rows = cur.fetchall()
for row in rows:
    (
        rid,
        rname,
        rnamekana,
        rpc,
        radd,
        rtel,
        remail,
        rqtybooks,
        rrdate,
        rddate,
        rmemo,
        rflg,
    ) = row
    #    print (row)

    print(f"削除する利用者情報　 \n 利用者ID　:　{rid} \n 利用者名　:{rname} \n 利用者名（カナ） :{rnamekana} \n")
# 利用者の借用状況（貸出数）


# 選択した利用者が図書を借用中である？

if rqtybooks >= 1:
    print(f"警告！！！　利用者の現在の貸出数は {rqtybooks}　冊です。")
    # 「図書借用中の利用者を削除できません。」表示
    print("「図書借用中の利用者を削除できません。」\n　すべて返却されてから削除してください。")
#    print(f"返却督促先:電話　{rtel} E-mail {remail} ")

else:

    confirm = int(input(f"本当に{rname}さんを削除してよいですか？　OK=0 NO=1"))
    if confirm == 1:
        print("利用者削除を取りやめてメインメニューに戻ります。")
    else:
        # 削除登録を選択する＝削除フラグ(d-flag)を0にする
        cur.execute("update customer set d_flag = 0 where c_id = %s", did)
        #    print(cur.rowcount,"件、削除しました。")
        # 正常に処理できた場合
        print(f"利用者　{rname} を削除しました。　\n メインメニューに戻ります。")

# 「利用者～を削除しました。」を表示。
# やり直し
conn.commit()
cur.close()
conn.close()

# return
