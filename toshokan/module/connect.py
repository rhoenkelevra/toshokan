# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 15:27:37 2021

@author: user24
"""
import mysql.connector as mydb
# =============================================================================
#                                    コネクション
# =============================================================================


def connect():
    conn = mydb.connect(
        host="localhost",
        port="3306",
        user="root",
        password="rfr689022",
        database="toshokan"
    )
    return conn