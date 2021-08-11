# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 14:34:58 2021

@author: user24
"""
from module.logs.returnBook import returnBook


# =============================================================================
#   ログイン
# =============================================================================




# =============================================================================
#   メニュー
# =============================================================================


# 
while True:
    print("=" * 10, "メニュー", "=" * 10)
    menu_choice = int(input("①・図書貸出　②・図書返却　③・図書管理　④・利用者管理　⑤・管理者用　⑨・ログアウト \n>"))
    
    
    if menu_choice == 1:
        pass

    if menu_choice == 2:
        
        returnBook()
           
            
    if menu_choice == 3:
        pass
    
    if menu_choice == 4:
        pass
    
    if menu_choice == 5:
        pass
    
    if menu_choice == 9:
        pass
