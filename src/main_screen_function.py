import tkinter as tk

import base_function as bftn
import button_function as btftn
import account_data as acc
import config_set as con




def gen_notebook(Frame_class, N_List, user_id, width, height):    
    notebook = Frame_class.gen_notebook(width, height)
    notebook.place(x=530, rely=0.1)
    
    student_info = bftn.student_info()
    consult_content = bftn.consult_content()
    exam_content = bftn.exam_content()
    
    tab1 = tk.Frame(notebook)
    notebook.add(tab1, text="기본정보")
    basic_info(tab1, student_info, user_id)
    
    tab2 = tk.Frame(notebook)
    notebook.add(tab2, text="수업정보")
    class_info(tab2, student_info, N_List, user_id)
    
    tab3 = tk.Frame(notebook)
    notebook.add(tab3, text="상담내용")
    consult_date_list = consult_info(tab3, consult_content, user_id)
    
    tab4 = tk.Frame(notebook)   
    notebook.add(tab4, text="시험결과")
    exam_type_list = info_exam(tab4, exam_content, user_id)
    
    lookup_btn = Frame_class.gen_button_fs("조회", lambda: btftn.lookup_info(Frame_class, N_List, student_info,
                                                              consult_content, consult_date_list, exam_type_list), 415, 320)
    N_List.bind("<Double-1>", lambda event: Frame_class.on_double_click_btn(event, lookup_btn))
    
    
    
def Teacher_list_button(Frame_class, T_List, C_List, N_List, user_id):
    
    var = tk.StringVar()
    var1 = tk.StringVar()
    
    
    lookup_btn = Frame_class.gen_button_fs("조회", lambda: btftn.lookup_C_listbox(Frame_class, C_List, T_List, N_List), 115, 320)
    T_List.bind("<Double-1>", lambda event: Frame_class.on_double_click_btn(event, lookup_btn))
    
    T_entry = Frame_class.gen_entry(var, 50, 280, 15)
    
    for author_id in acc.T_list_button_authority:
        if acc.acc_to_tname[user_id.get()] == author_id:
            Frame_class.gen_button_fs("수정", lambda: btftn.modify_T_listbox(Frame_class, T_List, var1), 115, 360)        
            Frame_class.gen_button_fs("추가", lambda: btftn.add_T_listbox(Frame_class, T_List, T_entry, f"{con.column[0]}", var.get()), 55, 400)
            Frame_class.gen_button_fs("삭제", lambda: btftn.delete_T_listbox(Frame_class, T_List), 115, 400)
        
        
    
def Class_list_button(Frame_class, C_List, N_List, user_id):
    
    var = tk.StringVar()
    var1 = tk.StringVar()
    C_entry = Frame_class.gen_entry(var, 200, 280, 15)
    
    Frame_class.gen_button_fs("수정", lambda: btftn.modify_C_listbox(Frame_class, C_List, user_id, var1), 265, 360)
    lookup_btn = Frame_class.gen_button_fs("조회", lambda: btftn.lookup_N_listbox(Frame_class, C_List, N_List), 265, 320)
    C_List.bind("<Double-1>", lambda event: Frame_class.on_double_click_btn(event, lookup_btn))
    
    Frame_class.gen_button_fs("추가", lambda: btftn.add_C_listbox(Frame_class, C_List, C_entry, user_id,
                                                                f"{con.column[0]}, {con.column[1]}", var.get()), 205, 400)
    Frame_class.gen_button_fs("삭제", lambda: btftn.delete_C_listbox(Frame_class, C_List, user_id), 265, 400)
    
    
    
def Name_list_button(Frame_class, C_List, N_List, user_id):
    
    var = tk.StringVar()
    var1 = tk.StringVar()
    N_entry = Frame_class.gen_entry(var, 350, 280, 15)
    
    Frame_class.gen_button_fs("이동", lambda: btftn.transfer_N_listbox(Frame_class, user_id, N_List), 355, 360)
    Frame_class.gen_button_fs("수정", lambda: btftn.modify_N_listbox(Frame_class, N_List, user_id, var1), 415, 360)
    Frame_class.gen_button_fs("추가", lambda: btftn.add_N_listbox(Frame_class, N_List, N_entry, C_List, user_id,
                                                                f"{con.column[0]}, {con.column[1]}, {con.column[2]}", var.get()), 355, 400)
    Frame_class.gen_button_fs("삭제", lambda: btftn.delete_N_listbox(Frame_class, N_List, user_id), 415, 400)
    
    
    
def basic_info(tab, student_info, user_id):
    
    tab_class = bftn.window_set(tab)
    
    student_info.age_var = tk.StringVar()
    student_info.gender_var = tk.StringVar()
    student_info.school_var = tk.StringVar()
    student_info.grade_var = tk.StringVar()
    student_info.birth_var = tk.StringVar()
    student_info.st_HP_var = tk.StringVar()
    student_info.pa_HP_var = tk.StringVar()
    student_info.email_var = tk.StringVar()
    
    tab_class.insert_label_entry(student_info.age_var, "나이", 10, 10, 70, 10)
    tab_class.insert_label_entry(student_info.gender_var, "성별", 10, 35, 70, 35)
    tab_class.insert_label_entry(student_info.school_var, "학교", 10, 60, 70, 60)
    tab_class.insert_label_entry(student_info.grade_var, "학년", 10, 85, 70, 85)
    tab_class.insert_label_entry(student_info.birth_var, "생년월일", 10, 110, 70, 110)
    tab_class.insert_label_entry(student_info.st_HP_var, "학생 연락처", 193, 10, 285, 10, 12, 27)
    tab_class.insert_label_entry(student_info.pa_HP_var, "학부모 연락처", 193, 35, 285, 35, 12, 27)
    tab_class.insert_label_entry(student_info.email_var, "e-mail", 226, 60, 285, 60, 7, 27)
    student_info.address = tab_class.insert_label_text("주소", 240, 85, 285, 85, 7, 27, 3)
    student_info.etc = tab_class.insert_label_text("특이사항", 10, 145, 15, 170, 7, 66, 10)
    
    tab_class.gen_button_fs("입력", lambda: btftn.add_basic_info(tab_class, user_id, student_info), 440, 315)

    
    
def class_info(tab, student_info, N_List, user_id):
    
    tab_class = bftn.window_set(tab)
    
    student_info.course_var = tk.StringVar()
    student_info.class_day_var = tk.StringVar()
    student_info.day1_var = tk.StringVar()
    student_info.day2_var = tk.StringVar()
    student_info.day3_var = tk.StringVar()
    student_info.day1_start_var = tk.StringVar()
    student_info.day1_end_var = tk.StringVar()
    student_info.day2_start_var = tk.StringVar()
    student_info.day2_end_var = tk.StringVar()
    student_info.day3_start_var = tk.StringVar()
    student_info.day3_end_var = tk.StringVar()
    
    student_info.main_book_var = tk.StringVar()
    student_info.main_start_date_var = tk.StringVar()
    student_info.main_end_date_var = tk.StringVar()
    student_info.sub_book_var = tk.StringVar()
    student_info.sub_start_date_var = tk.StringVar()
    student_info.sub_end_date_var = tk.StringVar()
    student_info.text2_var = tk.StringVar()
    
    
    
    tab_class.gen_label_rely("● 수업 요일/시간", 10, 0.03)
    tab_class.insert_label_entry(student_info.course_var, "과정", 55, 40, 30, 40, E_width=6)
    tab_class.insert_label_entry(student_info.class_day_var, "요일", 165, 40, 125, 40, E_width=8)
    tab_class.gen_entry(student_info.day1_var, 30, 65, 3)
    tab_class.gen_label(":", 60, 65)
    tab_class.gen_entry(student_info.day1_start_var, 75, 65, 8)
    tab_class.gen_label("~", 140, 65)
    tab_class.gen_entry(student_info.day1_end_var, 160, 65, 8)
    
    tab_class.gen_entry(student_info.day2_var, 30, 90, 3)
    tab_class.gen_label(":", 60, 90)
    tab_class.gen_entry(student_info.day2_start_var, 75, 90, 8)
    tab_class.gen_label("~", 140, 90)
    tab_class.gen_entry(student_info.day2_end_var, 160, 90, 8)
    
    tab_class.gen_entry(student_info.day3_var, 30, 115, 3)
    tab_class.gen_label(":", 60, 115)
    tab_class.gen_entry(student_info.day3_start_var, 75, 115, 8)
    tab_class.gen_label("~", 140, 115)
    tab_class.gen_entry(student_info.day3_end_var, 160, 115, 8)
    
    student_info.text1 = tab_class.insert_label_text("● 특이사항", 125, 12, 250, 40, 40, 32, 10)
    
    
    tab_class.gen_label_rely("● 진행중인 교재", 10, 0.5)
    tab_class.insert_label_entry(student_info.main_book_var, "주 교재", 10, 200, 70, 200, E_width=19)
    tab_class.insert_label_entry(student_info.main_start_date_var, "시작일", 210, 200, 270, 200, E_width=10)
    tab_class.insert_label_entry(student_info.main_end_date_var, "종료일", 345, 200, 405, 200, E_width=10)
    tab_class.insert_label_entry(student_info.sub_book_var, "부 교재", 10, 225, 70, 225, E_width=19)
    tab_class.insert_label_entry(student_info.sub_start_date_var, "시작일", 210, 225, 270, 225, E_width=10)
    tab_class.insert_label_entry(student_info.sub_end_date_var, "종료일", 345, 225, 405, 225, E_width=10)
    tab_class.insert_label_entry(student_info.text2_var, "특이사항", 10, 250, 70, 250, E_width=58)
    
    tab_class.gen_button("주교재 시작", lambda: bftn.set_today(student_info.main_start_date_var), 70, 280)
    tab_class.gen_button("부교재 시작", lambda: bftn.set_today(student_info.sub_start_date_var), 159, 280)
    tab_class.gen_button("주교재 종료", lambda: bftn.set_today(student_info.main_end_date_var), 250, 280)
    tab_class.gen_button("부교재 종료", lambda: bftn.set_today(student_info.sub_end_date_var), 339, 280)
    tab_class.gen_button_bs("완료 항목으로 이동", lambda: btftn.textbook_complete(tab_class, user_id, student_info), 22, 1, 70, 310)
    # tab_class.gen_button_bs("완료된 교재", empty_function, 22, 1, 250, 310)
    tab_class.gen_button_bs("입력", lambda: btftn.add_class_info(tab_class, user_id, student_info), 6, 3, 428, 280)
    
    
    
def consult_info(tab, consult_content, user_id):
    
    tab_class = bftn.window_set(tab)
    
    tab_class.insert_label_entry(consult_content.subject_var, "상담주제", 10, 10, 75, 10, 7, 25)
    tab_class.insert_label_entry(consult_content.date_var, "상담일자", 283, 10, 348, 10, 7, 18)
    consult_content.content = tab_class.insert_label_text("상담내용", 10, 40, 15, 65, 7, 66, 17)
    
    option = []
    consult_date_cbox = tab_class.gen_combobox(option, 12, 15, 305)
    
    tab_class.gen_button_fs("조회", lambda: btftn.lookup_consult_info(tab_class, consult_content, consult_date_cbox), 256, 305)
    tab_class.gen_button_fs("수정", lambda: btftn.modify_consult_info(tab_class, consult_content, user_id), 316, 305)
    tab_class.gen_button_fs("삭제", lambda: btftn.delete_consult_info(tab_class, consult_content, consult_date_cbox, user_id), 376, 305)
    tab_class.gen_button_fs("입력", lambda: btftn.add_consult_info(tab_class, user_id, consult_content, consult_date_cbox), 436, 305)
    
    return consult_date_cbox


        
def info_exam(tab, exam_content, user_id):
    
    tab_class = bftn.window_set(tab)
        
    tab_class.gen_label("시험종류 선택", 10, 10)
    
    options = ["전체"]
    bftn.get_exam_list(options, con.exam_column[3], con.selected_st_name)
    
    exam_type_cbox = tab_class.gen_combobox(options, 12, 110, 10)
    
    exam_columns = ('col 1', 'col 2', 'col 3', 'col 4', 'col 5')
    tree = tab_class.gen_treeview(exam_columns, 10, 40)
    
    
    tree.heading('col 1', text='번호', command=lambda: tab_class.column_sort_numeric('col 1'))
    tree.heading('col 2', text='날짜', command=lambda: tab_class.column_sort('col 2'))
    tree.heading('col 3', text='시험종류', command=lambda: tab_class.column_sort('col 3'))
    tree.heading('col 4', text='시험범위', command=lambda: tab_class.column_sort('col 4'))
    tree.heading('col 5', text='점수', command=lambda: tab_class.column_sort_numeric('col 5'))
    
    tree.column('col 1', width=35)
    tree.column('col 2', width=85)
    tree.column('col 3', width=105)
    tree.column('col 4', width=190)
    tree.column('col 5', width=65)
        
    tab_class.gen_entry(exam_content.date_var, 40, 270, 11)
    tab_class.gen_entry(exam_content.exam_type_var, 128, 270, 14)
    tab_class.gen_entry(exam_content.exam_range_var, 237, 270, 25)
    tab_class.gen_entry(exam_content.score_var, 424, 270, 9)
    
    tree.bind("<Double-1>", lambda event: tab_class.on_double_click(event, exam_content))
    
    # tab_class.gen_button_bs("일괄입력", empty_function, 12, 2, 10, 300)
    tab_class.gen_button_fs("조회", lambda: btftn.lookup_exam_info(tab_class, exam_type_cbox, tree), 256, 305)
    tab_class.gen_button_fs("수정", lambda: btftn.modify_exam_info(tab_class, exam_content, tree, user_id), 316, 305)
    tab_class.gen_button_fs("삭제", lambda: btftn.delete_exam_info(tab_class, tree, user_id), 376, 305)
    tab_class.gen_button_fs("입력", lambda: btftn.add_exam_info(tab_class, tree, exam_content, user_id), 436, 305)
    
    return exam_type_cbox
  

    
def empty_function():
    a=1
    

    