# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 11:48:08 2021

@author: user24
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 13:29:57 2021

@author: user24
"""


import mysql.connector as mydb
from mysql.connector import errorcode

con = mydb.connect(
    host="localhost",
    port="3306",
    user="root",
    password="pass",
    database="toshokan",
)

cursor = con.cursor(buffered=True)

TABLES = {}

TABLES["users"] = (
    "CREATE TABLE `users` ("
    "  `u_id` int(11) NOT NULL  AUTO_INCREMENT,"
    "  `u_name` varchar(255) NOT NULL,"
    "  `u_pass` varchar(255) NOT NULL,"
    "  `d_flag` tinyint(1) DEFAULT 1,"  # 1: ある 0:削除済
    "  PRIMARY KEY (`u_id`)"
    ") ENGINE=InnoDB  AUTO_INCREMENT=1000"
)

TABLES["customers"] = (
    "CREATE TABLE `customers` ("
    "  `c_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `c_name` varchar(20) NOT NULL,"
    "  `c_name_kana` varchar(50) NOT NULL,"
    "  `post_code` varchar(8) NOT NULL,"
    "  `address` varchar(255) NOT NULL,"
    "  `tel` varchar(20) NOT NULL,"
    "  `email` varchar(50),"
    "  `qtybooks` int(10) DEFAULT 0,"  # 3まで
    "  `register_date` DATE DEFAULT(CURRENT_DATE), "
    "  `delete_date` date,"
    "  `memo` varchar(255) DEFAULT '',"
    "  `d_flag` tinyint(1) DEFAULT 1,"  # 1: ある 0:削除済
    "  PRIMARY KEY (`c_id`)"
    ") ENGINE=InnoDB"
)

TABLES["books"] = (
    "CREATE TABLE `books` ("
    "  `b_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `isbn` char(20) NOT NULL,"
    "  `title` varchar(40) NOT NULL,"
    "  `author` varchar(40) NOT NULL ,"
    "  `p_name` varchar(40) NOT NULL,"
    "  `p_date` date NOT NULL,"
    "  `status` tinyint(1) DEFAULT 1,"  # 1:ある 0:貸出済
    "  `d_flag` tinyint(1) DEFAULT 1,"  # 1: ある 0:削除済
    "  PRIMARY KEY (`b_id`)"
    ") ENGINE=InnoDB"
)

TABLES["logs"] = (
    "CREATE TABLE `logs` ("
    "  `l_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `u_id` int(11) NOT NULL,"
    "  `b_id` int(11) NOT NULL,"
    "  `c_id` int(11) NOT NULL,"
    "  `out_date` date,"
    "  `in_limit_date` date,"
    "  `in_date` date,"  
    "  `d_flag` tinyint(1) DEFAULT 1,"
    "  `memo` varchar(255) DEFAULT '',"
    "  PRIMARY KEY (`l_id`),"
    "  FOREIGN KEY (u_id) REFERENCES `users` (`u_id`),"
    "  FOREIGN KEY (b_id) REFERENCES `books` (`b_id`),"
    "  FOREIGN KEY (c_id) REFERENCES `customers` (`c_id`)"
    ") ENGINE=InnoDB"
)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end="")
        cursor.execute(table_description)
    except mydb.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


cursor.close()
con.close()
