import tkinter as tk

import base_function as bftn
import button_function as btftn
import account_data as acc




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
    
    
    
    
def Teacher_list_button(Frame_class, T_List, user_id):
    
    for author_id in acc.T_list_button_authority:
        if acc.acc_to_tname[user_id.get()] == author_id:
            var = tk.StringVar()
            Frame_class.gen_button_fs("수정", empty_function, 115, 360)
            T_entry = Frame_class.gen_entry(var, 50, 280, 15)
            Frame_class.gen_button_fs("추가", lambda: btftn.add_T_listbox(Frame_class, T_List, T_entry, "teacher", var.get()), 55, 400)
            Frame_class.gen_button_fs("삭제", lambda: btftn.delete_T_listbox(Frame_class, T_List), 115, 400)
        
    
def Class_list_button(Frame_class, C_List, T_List, user_id):
    
    var = tk.StringVar()
    
    Frame_class.gen_button_fs("수정", empty_function, 265, 360)
    Frame_class.gen_button_fs("조회", lambda: btftn.lookup_C_listbox(Frame_class, C_List, T_List), 265, 320)
    
    C_entry = Frame_class.gen_entry(var, 200, 280, 15)
    Frame_class.gen_button_fs("추가", lambda: btftn.add_C_listbox(Frame_class, C_List, C_entry, T_List, user_id,
                                                                "teacher, class_name", var.get()), 205, 400)
    
    Frame_class.gen_button_fs("삭제", lambda: btftn.delete_C_listbox(Frame_class, C_List, user_id), 265, 400)
    
    
def test_function(T_list, var):
    index = T_list.curselection()
    item = str(T_list.get(index))
    print(len(item))
    print(item[2:len(item)-3])
    print(str(var.get()))
    # print(T_list.get(index)
    print(item)
    
    
    
def Name_list_button(Frame_class, N_List, C_List, user_id):
    
    var = tk.StringVar()
    
    Frame_class.gen_button_fs("이동", empty_function, 355, 360)
    Frame_class.gen_button_fs("수정", empty_function, 415, 360)
    Frame_class.gen_button_fs("조회", empty_function, 415, 320)
    
    N_entry = Frame_class.gen_entry(var, 350, 280, 15)
    Frame_class.gen_button_fs("추가", lambda: btftn.add_N_listbox(Frame_class, N_List, N_entry, C_List, user_id,
                                                                "teacher, class_name, name", var.get()), 355, 400)
    Frame_class.gen_button_fs("삭제", empty_function, 415, 400)
    
    
    
def info_basic(tab):
    
    tab_class = bftn.window_set(tab)
    
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
    
    tab_class.insert_label_entry(age_var, "나이", 10, 10, 70, 10)
    tab_class.insert_label_entry(gender_var, "성별", 10, 35, 70, 35)
    tab_class.insert_label_entry(school_var, "학교", 10, 60, 70, 60)
    tab_class.insert_label_entry(grade_var, "학년", 10, 85, 70, 85)
    tab_class.insert_label_entry(birth_var, "생년월일", 10, 110, 70, 110)
    tab_class.insert_label_entry(st_ph_var, "학생 연락처", 193, 10, 285, 10, L_width=12, E_width=25)
    tab_class.insert_label_entry(pa_ph_var, "학부모 연락처", 193, 35, 285, 35, L_width=12, E_width=25)
    tab_class.insert_label_entry(email_var, "e-mail", 226, 60, 285, 60, L_width=7, E_width=25)
    tab_class.insert_label_text("주소", 240, 85, 285, 85, L_width=7, T_width=25, height=3)
    tab_class.insert_label_text("특이사항", 10, 145, 10, 170, T_width=68, height=10)
    
    tab_class.gen_button_fs("입력", empty_function, 440, 315)

    
    
    
def info_class(tab):
    
    tab_class = bftn.window_set(tab)
    
    main_book_var = tk.StringVar()
    main_start_date_var = tk.StringVar()
    main_end_date_var = tk.StringVar()
    sub_book_var = tk.StringVar()
    sub_start_date_var = tk.StringVar()
    sub_end_date_var = tk.StringVar()
    text_var = tk.StringVar()
    
    tab_class.gen_label_rely("● 진행중인 교재", 10, 0.03)
    tab_class.insert_label_entry(main_book_var, "주 교재", 10, 40, 70, 40, E_width=19)
    tab_class.insert_label_entry(main_start_date_var, "시작일", 210, 40, 270, 40, E_width=10)
    tab_class.insert_label_entry(main_end_date_var, "종료일", 345, 40, 405, 40, E_width=10)
    tab_class.insert_label_entry(sub_book_var, "부 교재", 10, 65, 70, 65, E_width=19)
    tab_class.insert_label_entry(sub_start_date_var, "시작일", 210, 65, 270, 65, E_width=10)
    tab_class.insert_label_entry(sub_end_date_var, "종료일", 345, 65, 405, 65, E_width=10)
    tab_class.insert_label_entry(text_var, "특이사항", 10, 90, 70, 90, E_width=58)
    
    tab_class.gen_button("주교재 시작", empty_function, 70, 120)
    tab_class.gen_button("부교재 시작", empty_function, 159, 120)
    tab_class.gen_button("주교재 종료", empty_function, 250, 120)
    tab_class.gen_button("부교재 종료", empty_function, 339, 120)
    tab_class.gen_button_bs("완료 항목으로 이동", empty_function, 22, 1, 70, 150)
    tab_class.gen_button_bs("완료된 교재", empty_function, 22, 1, 250, 150)
    tab_class.gen_button_bs("입력", empty_function, 6, 3, 428, 120)
    
def info_consult(tab):
    tab_class = bftn.window_set(tab)
    tab_class.gen_label_rely("● 상담일", 10, 0.03)
    tab_class.gen_label_rely("● 상담기록", 10, 0.5)
    # tab_class.gen_button
    # t_variable = tk.StringVar()
    
    
def info_exam(tab):
    t_variable = tk.StringVar()
    
    
def empty_function():
    a=1
    

    