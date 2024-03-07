import tkinter as tk
import base_function as bftn
import config_set as con
import login_screen_function as lsf


def run_login_screen(login_wd):
    
    login_screen = bftn.window_set(login_wd)
    login_screen.set_title(con.login_screen_title)
    login_screen.set_size(con.login_screen_size)
    login_screen.insert_image(con.logo_directory, 10, 10)
    # 아이콘 바꾸기

    user_id = tk.StringVar()
    user_password = tk.StringVar()
        
    login_screen.insert_label_entry(user_id, "아이디", 35, 115, 105, 115, L_width=8, E_width=19)
    login_screen.insert_label_entry_show(user_password, "비밀번호", "*", 35, 140, 105, 140, L_width=8, E_width=19)
    login_screen.gen_button_bs("회원가입", lambda: lsf.password_generator(login_screen), 7, 1, 45, 200)
    login_screen.gen_button_bs("로그인", lambda: lsf.login_and_run_main_screen(login_screen, user_id, user_password), 7, 1, 115, 200)
    login_screen.gen_button_bs("종료", login_screen.clear_wd, 7, 1, 185, 200)
    
    login_screen.gen_label("<<<            환영합니다           >>>", 40, 170)
 
        
    
def empty_function():
    a=1
    
    

        