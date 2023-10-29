import tkinter as tk
from tkinter import ttk

import base_function as bftn


def list_box(Frame, pos):
    libInsert = tk.Listbox(Frame, width=13, height=14, selectmode="single")
    libInsert.insert(0, "부원장")
    libInsert.configure(font=10)
    libInsert.place(x=pos, rely=0.1)
    
    
def gen_notebook(Frame_class, width, height):    
    notebook = Frame_class.gen_notebook(width, height)
    notebook.place(x=530, rely=0.1)
    
    tab1 = tk.Frame(notebook)
    notebook.add(tab1, text="기본정보")
    info_basic(tab1)
    
    tab2 = tk.Frame(notebook)
    notebook.add(tab2, text="수업정보")
    info_class(tab2)
    
    tab3 = tk.Frame(notebook)
    notebook.add(tab3, text="상담내용")
    info_consult(tab3)
    
    tab4 = tk.Frame(notebook)   
    notebook.add(tab4, text="시험결과")
    info_exam(tab4)
    
    
    
    
def Teacher_list_button(Frame_class):
    Frame_class.gen_button_fs("수정", empty_function, 115, 360)
    Frame_class.gen_button_fs("추가", empty_function, 55, 400)
    Frame_class.gen_button_fs("삭제", empty_function, 115, 400)
    
def Class_list_button(Frame_class):
    Frame_class.gen_button_fs("수정", empty_function, 265, 360)
    Frame_class.gen_button_fs("추가", empty_function, 205, 400)
    Frame_class.gen_button_fs("삭제", empty_function, 265, 400)
    
def Name_list_button(Frame_class):
    Frame_class.gen_button_fs("이동", empty_function, 355, 360)
    Frame_class.gen_button_fs("수정", empty_function, 415, 360)
    Frame_class.gen_button_fs("조회", empty_function, 415, 320)
    Frame_class.gen_button_fs("추가", empty_function, 355, 400)
    Frame_class.gen_button_fs("삭제", empty_function, 415, 400)
    
    
    
def info_basic(tab):
    
    age_var = tk.StringVar()
    gender_var = tk.StringVar()
    school_var = tk.StringVar()
    grade_var = tk.StringVar()
    birth_var = tk.StringVar()
    st_ph_var = tk.StringVar()
    pa_ph_var = tk.StringVar()
    email_var = tk.StringVar()
    # address_var = tk.StringVar()
    # add_info_var = tk.StringVar()
    
    bftn.insert_label_entry(tab, age_var, "나이", 10, 10, 70, 10)
    bftn.insert_label_entry(tab, gender_var, "성별", 10, 35, 70, 35)
    bftn.insert_label_entry(tab, school_var, "학교", 10, 60, 70, 60)
    bftn.insert_label_entry(tab, grade_var, "학년", 10, 85, 70, 85)
    bftn.insert_label_entry(tab, birth_var, "생년월일", 10, 110, 70, 110)
    bftn.insert_label_entry(tab, st_ph_var, "학생 연락처", 193, 10, 285, 10, L_width=12, E_width=25)
    bftn.insert_label_entry(tab, pa_ph_var, "학부모 연락처", 193, 35, 285, 35, L_width=12, E_width=25)
    bftn.insert_label_entry(tab, email_var, "e-mail", 226, 60, 285, 60, L_width=7, E_width=25)
    bftn.insert_label_text(tab, "주소", 226, 85, 285, 85, L_width=7, T_width=25, height=3)
    bftn.insert_label_text(tab, "특이사항", 10, 145, 10, 170, T_width=68, height=10)
    
    bftn.gen_button_fs(tab, "입력", empty_function, 440, 315)

    
    
    
def info_class(tab):
    t_variable = tk.StringVar()
    
    
def info_consult(tab):
    t_variable = tk.StringVar()
    
    
def info_exam(tab):
    t_variable = tk.StringVar()
    
    
def empty_function():
    a=1
    

    