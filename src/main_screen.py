import tkinter as tk
import base_function as baseftn
# import config_set as con

from tkinter import ttk



def run_main_screen(main_screen):
    
    top_frame(main_screen)
    mid_frame(main_screen)
    bot_frame(main_screen)
    

    
    
def top_frame(main_screen):
    Frame_1 = main_screen.gen_Frame(1, 110, "blue")
    Frame_1.pack(side = tk.TOP, fill=tk.X, expand=1)
    
    btnInsert = tk.Button(Frame_1, text="로고", width=30, height=5)
    btnInsert.place(x=10, y=10)
    
    # 공지사항 버튼 함수 추가
    btnInsert = tk.Button(Frame_1, text="공지사항", width=15, height=3)
    btnInsert.place(x=300, y=30)
    
    
    # 시간표 버튼 함수 추가
    btnInsert = tk.Button(Frame_1, text="시간표", width=15, height=3)
    btnInsert.place(x=420, y=30)
    
    
    # 일정 버튼 함수 추가
    btnInsert = tk.Button(Frame_1, text="일정", width=15, height=3)
    btnInsert.place(x=540, y=30)
    
    
    # 관리자모드 버튼 함수 추가
    btnInsert = tk.Button(Frame_1, text="관리자 모드", command=root_mod)
    btnInsert.place(x=1000, y=10)
    
    
    
    
def mid_frame(main_screen):
    Frame_2 = main_screen.gen_Frame(1, 510, "green")
    Frame_2.pack(side = tk.TOP, fill=tk.X, expand=1)
    
    lbInsert = tk.Label(Frame_2, text="선생님", font=10)
    lbInsert.place(x=100, rely=0.05)
    list_box(Frame_2, 50)
    Teacher_list_button(Frame_2)
    
    
    lbInsert = tk.Label(Frame_2, text="반 이름", font=10)
    lbInsert.place(x=250, rely=0.05)
    list_box(Frame_2, 200)
    Class_list_button(Frame_2)
    
    lbInsert = tk.Label(Frame_2, text="이름", font=10)
    lbInsert.place(x=400, rely=0.05)
    list_box(Frame_2, 350)
    Name_list_button(Frame_2)
    
    lbInsert = tk.Label(Frame_2, text="내용", font=10)
    lbInsert.place(x=530, rely=0.05)
    
    gen_notebook(Frame_2, 500, 350)
    

    
    
def bot_frame(main_screen):
    Frame_3 = main_screen.gen_Frame(1, 100, "yellow")
    Frame_3.pack(side = tk.BOTTOM, fill=tk.X, expand=1)
    
    
    
    
    
    
def root_mod():
    window = tk.Tk()
    root_mod_wd = baseftn.window_set(window)
    root_mod_wd.set_title("관리자 모드")
    root_mod_wd.gen_button("종료", root_mod_wd.clear_wd)
    
    
def list_box(Frame, pos):
    libInsert = tk.Listbox(Frame, width=13, height=14, selectmode="single")
    libInsert.insert(0, "부원장")
    libInsert.configure(font=10)
    libInsert.place(x=pos, rely=0.1)
    
    
def gen_notebook(Frame, width, height):
    notebook = ttk.Notebook(Frame, width=width, height=height)
    notebook.place(x=530, rely=0.1)
    
    tab1 = tk.Frame(notebook)
    notebook.add(tab1, text="기본정보")
    lbInsert = tk.Label(tab1, text="나이")
    lbInsert.place(x=10, y=10)
    
    tab2 = tk.Frame(notebook)
    notebook.add(tab2, text="수업정보")
    
    tab3 = tk.Frame(notebook)
    notebook.add(tab3, text="상담내용")
    
    tab4 = tk.Frame(notebook)   
    notebook.add(tab4, text="시험결과")
    
    
    
    
def Teacher_list_button(Frame):
    modify_button = tk.Button(Frame, text="수정", font=10)
    modify_button.place(x=115, y=360)
    add_button = tk.Button(Frame, text="추가", font=10)
    add_button.place(x=55, y=400)
    delete_button = tk.Button(Frame, text="삭제", font=10)
    delete_button.place(x=115, y=400)
    
    
    
    
def Class_list_button(Frame):
    modify_button = tk.Button(Frame, text="수정", font=10)
    modify_button.place(x=265, y=360)
    add_button = tk.Button(Frame, text="추가", font=10)
    add_button.place(x=205, y=400)
    delete_button = tk.Button(Frame, text="삭제", font=10)
    delete_button.place(x=265, y=400)
    


def Name_list_button(Frame):
    lookup_button = tk.Button(Frame, text="조회", font=10)
    lookup_button.place(x=355, y=360)
    modify_button = tk.Button(Frame, text="수정", font=10)
    modify_button.place(x=415, y=360)
    move_button = tk.Button(Frame, text="이동", font=10)
    move_button.place(x=415, y=320)
    add_button = tk.Button(Frame, text="추가", font=10)
    add_button.place(x=355, y=400)
    delete_button = tk.Button(Frame, text="삭제", font=10)
    delete_button.place(x=415, y=400)