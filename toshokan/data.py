import mysql.connector as mydb


def connect():
    conn = mydb.connect(
        host="localhost",
        port="3306",
        user="root",
        password="pass",
        database="toshokan"
    )
    return conn


# =============================================================================
#   User Table
# =============================================================================
def addUser():
    con = connect()
    cur = con.cursor()

    users = [
        #    u_name , u_pass
        ('suzuki', 'pass'),
        ('yamane', 'pass'),
        ('inoue', 'pass'),
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

    books = [
        # isbn      title     author         p      p_date       status, d_flag
        ('12345', 'example', 'JR Tolken', 'Intes', '2019-10-10', 1, 1),
        ('2345', 'aifja', 'Yokota', 'Intesc', '2019-02-22', 1, 1),
        ('098735', 'test', 'rene', 'Intesc', '2019-10-10', 1, 1),
        ('098735', 'test', 'rene', 'Intesc', '2019-10-10', 1, 1),
        ('098735', 'test', 'rene', 'Intesc', '2019-10-10', 1, 1),
        ('098735', 'test', 'rene', 'Intesc', '2019-10-10', 1, 1),
        ('098735', 'test', 'rene', 'Intesc', '2019-10-10', 1, 1),
        ('098735', 'test', 'rene', 'Intesc', '2019-10-10', 1, 1),
        ('098735', 'test', 'rene', 'Intesc', '2019-10-10', 1, 1),
        ('098735', 'test', 'rene', 'Intesc', '2019-10-10', 1, 1),
        ('098735', 'test', 'rene', 'Intesc', '2019-10-10', 1, 1),
        ('098735', 'test', 'rene', 'Intesc', '2019-10-10', 1, 1),
        ('098735', 'test', 'rene', 'Intesc', '2019-10-10', 1, 1),

    ]
    cur.executemany(
        "insert into books (isbn, title, author, p_name, p_date, status, d_flag) values(%s, %s, %s, %s, %s, %s, %s)", books)

    con.commit()
    print("登録しました。")
    cur.close()


# =============================================================================
#   Customer Table
# =============================================================================


def addCustomer():
    con = connect()
    cur = con.cursor()

    customer = [
        # c_name    #c_name_kana post_code address tel            qtybooks
        ("yamauchi", "yamauchi", 5673994, 'aichi', '909-0999-9999', 3, ),
        ("sara", "sara", 5673994, 'aichi', '909-0999-9999', 1),
        ("nagamine", "nagamine", 5673994, 'aichi', '909-0999-9999', 1),
        ("yoshida", "yoshida", 5673994, 'aichi', '909-0999-9999', 2),

    ]
    cur.executemany(
        "insert into customer (c_name, c_name_kana, post_code, address, tel, qtybooks) values(%s, %s, %s, %s, %s, %s)", customer)

    con.commit()
    print("登録しました。")
    cur.close()
    con.close()


# =============================================================================
#   Log Table
# =============================================================================


def addLog():
    con = connect()
    cur = con.cursor()

    log = [
        # u_id,b_id,c_id,out_date
        (1, 1, 3, '2020/06/12'),
        (1, 2, 3, '2020/06/12'),
        (1, 3, 2, '2020/06/12'),
        (1, 4, 2, '2020/06/12'),
        (1, 5, 1, '2020/06/12'),
        (1, 6, 1, '2020/06/12'),
    ]
    cur.executemany(
        "insert into log(u_id, b_id, c_id, out_date) values(%s, %s, %s, %s)", log)

    con.commit()
    print("登録しました。")
    cur.close()
    con.close()


# ==================================================================
# 先にこの３関数を呼び出す
# addUser()
# addCustomer()
# addBook()
# ==================================================================
# 最後にこれを呼び出す
addLog()
