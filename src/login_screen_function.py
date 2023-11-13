import tkinter as tk

import base_function as bftn
import config_set as con
import account_data as acc_data
import main_screen as ms



def login_and_run_main_screen(login_screen, user_id, user_password):
            
    account_info = acc_data.account_info
        
    ID_check = False
    for acc_id in account_info.keys():
        if user_id.get() == acc_id:
            ID_check = True
            
            if user_password.get() == account_info[user_id.get()]:
                login_screen.clear_wd()
                main_wd = tk.Tk()
                main_screen = bftn.window_set(main_wd)
                main_screen.set_title(con.main_screen_title)
                main_screen.set_size(con.main_screen_size)
                main_screen.set_fullscreen()
                ms.run_main_screen(main_screen, user_id)
                
            else:
                login_screen.label_ntxt("<<<  비밀번호를 확인해주세요  >>>")
                break
            
    if ID_check == False:
        login_screen.label_ntxt("<<<   아이디를 확인해주세요    >>>")