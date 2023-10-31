import tkinter as tk

import base_function as baseftn
import config_set as con
import main_screen_function as msf


def run_main_screen(main_screen):
       
    top_frame(main_screen)
    mid_frame(main_screen)
    bot_frame(main_screen)
    
    
    
def top_frame(main_screen):
    Frame_1 = main_screen.gen_Frame(1, 110, "blue")
    Frame_class = baseftn.window_set(Frame_1)
    Frame_class.pack(tk.TOP, tk.X, 1)
        
    
    # 로고 사진 변경
    Frame_class.insert_image(con.logo_directory, 10, 10)
    

    # 버튼 함수 추가
    Frame_class.gen_button_bs("공지사항", empty_function, 15, 3, 300, 30)
    Frame_class.gen_button_bs("시간표", empty_function, 15, 3, 420, 30)
    Frame_class.gen_button_bs("일정", empty_function, 15, 3, 540, 30)
    Frame_class.gen_button("관리자 모드", root_mod, 1000, 10)
        
    
    
def mid_frame(main_screen):
    Frame_2 = main_screen.gen_Frame(1, 510, "black")
    Frame_class = baseftn.window_set(Frame_2)
    Frame_class.pack(tk.TOP, tk.X, 1)
    
    Frame_class.gen_label_rely_fs("선생님", 100, 0.05)
    msf.list_box(Frame_2, 50)
    msf.Teacher_list_button(Frame_class)
    
    Frame_class.gen_label_rely_fs("반 이름", 250, 0.05)
    msf.list_box(Frame_2, 200)
    msf.Class_list_button(Frame_class)
    
    Frame_class.gen_label_rely_fs("이름", 400, 0.05)
    msf.list_box(Frame_2, 350)
    msf.Name_list_button(Frame_class)
    
    Frame_class.gen_label_rely_fs("내용", 530, 0.05)
    msf.gen_notebook(Frame_class, 500, 350)
    
    
    
def bot_frame(main_screen):
    Frame_3 = baseftn.window_set(main_screen.gen_Frame(1, 100, "yellow"))
    Frame_3.pack(tk.BOTTOM, tk.X, 1)
    
    
    
def root_mod():
    window = tk.Tk()
    root_mod_wd = baseftn.window_set(window)
    root_mod_wd.set_title("관리자 모드")
    root_mod_wd.gen_button("종료", root_mod_wd.clear_wd, 30, 30)
    
    
def empty_function():
    a=1
    
   