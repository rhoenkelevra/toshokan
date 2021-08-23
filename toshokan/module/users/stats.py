# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 13:43:48 2021

@author: user24
"""

from module.setup.connect import connect
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
font = font_manager.FontProperties(fname='C:/WINDOWS/Fonts/MS GOTHIC.TTC')
from matplotlib.ticker import MaxNLocator

def showStats():
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("select b_id, count(b_id) from logs group by b_id")
    
    lending_amt = []
    customers = []
    res = cur.fetchall()
    for row in res:
        lending_amt.append(row[1])
        customers.append(row[0])
        print(f"{row[0]} has used {row[1]} times")
        
    
    print(customers)
    print(lending_amt)
    
        
    plt.barh(customers, lending_amt) 
    plt.xlabel("貸出数回", fontname="MS Gothic")
    ax = plt.figure().gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=5))
  
    plt.ylabel("図書ＩＤ", fontname="MS Gothic")
    plt.gca().invert_yaxis()
    plt.show()
        
    cur.close()
    conn.close()
    
    
showStats()