import mysql.connector as mydb


def connect():
    conn = mydb.connect(
        host="localhost",
        port="3306",
        user="root",
        password="rfr689022",
        database="toshokan"
    )
    return conn


# =============================================================================
#
# =============================================================================
def addUser():
    con = connect()
    cur = con.cursor()

    users = [
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
#
# =============================================================================


def addBook():
    con = connect()
    cur = con.cursor()

    books = [
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
#
# =============================================================================


def addCustomer():
    con = connect()
    cur = con.cursor()

    customer = [
        ("hello", "hello", 5673994, 'aichi', '909-0999-9999'),
        ("hi", "hi", 5673994, 'aichi', '909-0999-9999'),
        ("bye", "hi", 5673994, 'aichi', '909-0999-9999'),
        ("john", "hello", 5673994, 'aichi', '909-0999-9999'),

    ]
    cur.executemany(
        "insert into customer (c_name, c_name_kana, post_code, address, tel) values(%s, %s, %s, %s, %s)", customer)

    con.commit()
    print("登録しました。")
    cur.close()
    con.close()


# =============================================================================
#
# =============================================================================


def addLog():
    con = connect()
    cur = con.cursor()

    log = [

        (1, 1, 3, '2020-06-12', 'nashi'),
        (1, 2, 3, '2020-06-12', 'nashi'),
        (1, 3, 2, '2020-06-12', 'nashi'),
        (1, 4, 2, '2020-06-12', 'nashi'),
        (1, 5, 1, '2020-06-12', 'nashi'),
        (1, 6, 1, '2020-06-12', 'nashi'),
    ]
    cur.executemany(
        "insert into log(u_id, b_id, c_id, out_date, memo) values(%s, %s, %s, %s, %s)", log)

    con.commit()
    print("登録しました。")
    cur.close()
    con.close()


# addUser()
# addCustomer()
# addBook()
addLog()
