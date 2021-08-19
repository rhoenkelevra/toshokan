import mysql.connector as mydb


def connect():
    conn = mydb.connect(
        host="localhost", port="3306", user="root", password="pass", database="toshokan"
    )
    return conn


# =============================================================================
#   User Table　図書館係員
# =============================================================================
def addUser():
    con = connect()
    cur = con.cursor()
# ログインID：数字のみ（自動連番：1000～）
# パスワード：半角英数字最小4文字、最大8文字
    users = [
        #    u_name , u_pass
        ("井上　香織", "pass01"),
        ("稲吉　歩美", "pass08"),
        ("鈴木　幸裕", "pass09"),
        ("Rhoen Rene Frederik", "pass13"),
        ("山根　佑希絵", "pass15"),
        ("横田　萌", "pass19"),
    ]
    cur.executemany("insert into users (u_name, u_pass) values(%s, %s)", users)

    con.commit()
    print("登録しました。")
    cur.close()
    con.close()


# =============================================================================
#   Books Table
# =============================================================================


def addBook():
    con = connect()
    cur = con.cursor()
# 図書名：最大40文字
# 図書ID：数字のみ（自動連番）

    books = [
        # isbn      title     author         p_name      p_date       status, d_flag
        ('978-4798024035','わかりやすいJava入門編','山田太郎','秀和システム ','2009-10-01',1,1),
        ('978-4797344387','基礎からのMySQL ','山田太郎','ソフトバンククリエイティブ','2007-12-26',1,1),
        ('978-4797339536','明解Java　入門編','山田太郎','ソフトバンククリエイティブ','2007-08-08',1,1),
        ('978-4844330868','スッキリわかるJava入門','山田太郎','インプレスジャパン','2011-10-07 ',1,1),
        ('978-4774138213','図解でよくわかる ネットワークの重要用語解説','山田太郎','技術評論社','2009-03-25 ',1,1),
        ('978-4839919849','30日でできる! OS自作入門','山田太郎','毎日コミュニケーションズ ','2006-03-01 ',1,1),
        ('978-4797311129','オブジェクト指向における再利用のためのデザインパターン','山田太郎','ソフトバンククリエイティブ','1999-10-01',1,1),
        ('978-4877832391','12ステップで作る組込みOS自作入門','山田太郎','カットシステム','2010-05-01',1,1),
        ('978-4797359091','ネットワーク超入門講座','山田太郎','ソフトバンククリエイティブ','2010-03-20',1,1),
        ('978-4798027685','Visual Basic 2010逆引き大全555の極意','山田太郎','秀和システム','2010-11-01',1,1),
        ('978-4894714991','Effective Java','山田太郎','ピアソンエデュケーション','2008-11-27',1,1),
        ('978-4781910246','リレーショナルデータベース入門―データモデル・SQL','山田太郎','サイエンス社','2003-03-01',1,1),
        ('978-4822294229','プログラムを作ろう Microsoft Visual Basic 2010 入門','山田太郎','日経BP社','2010-09-02',1,1),
        ('978-4839933142','よくわかるPHPの教科書','山田太郎','毎日コミュニケーションズ','2010-09-14',1,1),
        
        
    ]
    cur.executemany(
        "insert into books (isbn, title, author, p_name, p_date, status, d_flag) values(%s, %s, %s, %s, %s, %s, %s)", books)

    con.commit()
    print("登録しました。")
    cur.close()
    con.close()

# =============================================================================
#   Customer Table 利用者
# =============================================================================


def addCustomer():
    con = connect()
    cur = con.cursor()

# 利用者名最大20文字
# 利用者ID数字のみ（自動連番）

    customer = [
        # c_name    #c_name_kana post_code address tel
        ("川場　隆","カワバタ　タカシ","453-0015","愛知県名古屋市中村区椿町21-2 第2太閤ビル5F","052-485-8407"),
        ("西沢　夢路","ニシザワ　ユメジ","509-0109","岐阜県各務原市テクノプラザ1-1 本館213","058-379-0335"),
        ("柴田　望洋","シバタ　ボウヨウ","460-8640","名古屋市中区錦2-14-25 ヤマウチビル2F","052-855-3740"),
    ]
    cur.executemany(
        "insert into customers (c_name, c_name_kana, post_code, address, tel) values(%s, %s, %s, %s, %s)",
        customer,
    )

    con.commit()
    print("登録しました。")
    cur.close()
    con.close()



addUser()
addCustomer()
addBook()
