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
            
            if bftn.get_string_hash(user_password.get()) == account_info[user_id.get()]:
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
        
        
        
def password_generator(login_screen):
    
    sub_wd = login_screen.sub_wd()
    sub_wd_class = bftn.window_set(sub_wd)
    sub_wd_class.set_title("비밀번호 생성")
    sub_wd_class.set_size("285x200")
    
    
    password = tk.StringVar()
    password_check = tk.StringVar()
    
    sub_wd_class.gen_label("비밀번호", 10, 10)
    sub_wd_class.gen_entry(password, 100, 10, 24)
    sub_wd_class.gen_label("비밀번호 확인", 10, 45)
    sub_wd_class.gen_entry(password_check, 100, 45, 24)
    
    hashbox = sub_wd_class.gen_textbox(10, 140, 37, 3)
        
    sub_wd_class.gen_button("생성", lambda: gen_hashvalue(password, password_check, hashbox), 80, 90)
    sub_wd_class.gen_button("취소", sub_wd_class.clear_wd, 170, 90)
        
    
    
def gen_hashvalue(password, password_check, hashbox):
    
    if f"{password.get()}" == f"{password_check.get()}":
        hashval = bftn.get_string_hash(password.get())
        hashbox.insert(tk.END, hashval)
    else:
        hashbox.insert(tk.END, "비밀번호가 일치하지 않습니다.")