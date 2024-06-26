import tkinter as tk

import base_function as bftn
import config_set as con
import main_screen_function as msf
import account_data as acc


def run_main_screen(main_screen, user_id):
       
    bftn.config_set(user_id)
    top_frame(main_screen, user_id)
    mid_frame(main_screen, user_id)
    bot_frame(main_screen)
    
    
    
    
    
    
def top_frame(main_screen, user_id):
    Frame_1 = main_screen.gen_Frame(1, 110, "black")
    Frame_class = bftn.window_set(Frame_1)
    Frame_class.pack(tk.TOP, tk.X, 1)
        
    
    # 로고 사진 변경
    Frame_class.insert_image(con.logo_directory, 10, 10)
    

    # 버튼 함수 추가
    # Frame_class.gen_button_bs("공지사항", empty_function, 15, 3, 300, 30)
    # Frame_class.gen_button_bs("시간표", empty_function, 15, 3, 420, 30)
    # Frame_class.gen_button_bs("일정", empty_function, 15, 3, 540, 30)
    Frame_class.gen_button("관리자 모드", lambda: root_mod(Frame_class, user_id), 1000, 10)
        
    
    
def mid_frame(main_screen, user_id):
    Frame_2 = main_screen.gen_Frame(1, 510, "black")
    Frame_class = bftn.window_set(Frame_2)
    Frame_class.pack(tk.TOP, tk.X, 1)
    
    Frame_class.insert_image_orig(con.mid_frame_image, -5, -2)
    
    Frame_class.gen_label_rely_fs("선생님", 105, 0.05)
    T_List = Frame_class.gen_listbox_fs(50, 0.1)
    Frame_class.gen_label_rely_fs("반 이름", 250, 0.05)
    C_List = Frame_class.gen_listbox_fs(200, 0.1)
    Frame_class.gen_label_rely_fs("이름", 420, 0.05)
    N_List = Frame_class.gen_listbox_fs(350, 0.1)
    Frame_class.gen_label_rely_fs("내용", 530, 0.05)
    
    bftn.show_list_box(T_List, con.column[0], con.column[0])
    
    msf.Teacher_list_button(Frame_class, T_List, C_List, N_List, user_id)   
    msf.Class_list_button(Frame_class, C_List, N_List, user_id)
    msf.Name_list_button(Frame_class, C_List, N_List, user_id)
    msf.gen_notebook(Frame_class, N_List, user_id, 500, 350)
    
    
    
def bot_frame(main_screen):
    Frame_3 = bftn.window_set(main_screen.gen_Frame(1, 100, "black"))
    Frame_3.pack(tk.BOTTOM, tk.X, 1)
    
    
    
def root_mod(Frame_class, user_id):
    for author_id in acc.root_mode_authority:
        if acc.acc_to_tname[user_id.get()] == author_id:
            sub_wd = Frame_class.sub_wd()
            root_mod_wd = bftn.window_set(sub_wd)
            root_mod_wd.set_title("관리자 모드")
            root_mod_wd.gen_button("종료", root_mod_wd.clear_wd, 30, 30)
            return 0
        
    sub_wd = Frame_class.sub_wd()
    bftn.Error_Box(sub_wd, "권한이 없습니다.")
        
        
    
def empty_function():
    a=1
    
   