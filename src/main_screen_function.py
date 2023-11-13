import tkinter as tk

import base_function as bftn
import button_function as btftn
import account_data as acc
import config_set as con




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
    
    
    
def Teacher_list_button(Frame_class, T_List, C_List, N_List, user_id):
    
    var = tk.StringVar()
    Frame_class.gen_button_fs("조회", lambda: btftn.lookup_C_listbox(Frame_class, C_List, T_List, N_List), 115, 320)
    T_entry = Frame_class.gen_entry(var, 50, 280, 15)
    
    for author_id in acc.T_list_button_authority:
        if acc.acc_to_tname[user_id.get()] == author_id:
            Frame_class.gen_button_fs("수정", empty_function, 115, 360)        
            Frame_class.gen_button_fs("추가", lambda: btftn.add_T_listbox(Frame_class, T_List, T_entry, f"{con.column_1}", var.get()), 55, 400)
            Frame_class.gen_button_fs("삭제", lambda: btftn.delete_T_listbox(Frame_class, T_List), 115, 400)
        
        
    
def Class_list_button(Frame_class, T_List, C_List, N_List, user_id):
    
    var = tk.StringVar()
    C_entry = Frame_class.gen_entry(var, 200, 280, 15)
    
    Frame_class.gen_button_fs("수정", empty_function, 265, 360)
    Frame_class.gen_button_fs("조회", lambda: btftn.lookup_N_listbox(Frame_class, C_List, N_List), 265, 320)
    Frame_class.gen_button_fs("추가", lambda: btftn.add_C_listbox(Frame_class, C_List, C_entry, user_id,
                                                                f"{con.column_1}, {con.column_2}", var.get()), 205, 400)
    Frame_class.gen_button_fs("삭제", lambda: btftn.delete_C_listbox(Frame_class, C_List, user_id), 265, 400)
    
    
    
def Name_list_button(Frame_class, C_List, N_List, user_id):
    
    var = tk.StringVar()
    N_entry = Frame_class.gen_entry(var, 350, 280, 15)
    
    Frame_class.gen_button_fs("이동", empty_function, 355, 360)
    Frame_class.gen_button_fs("수정", empty_function, 415, 360)
    Frame_class.gen_button_fs("조회", empty_function, 415, 320)
    Frame_class.gen_button_fs("추가", lambda: btftn.add_N_listbox(Frame_class, N_List, N_entry, C_List, user_id,
                                                                f"{con.column_1}, {con.column_2}, {con.column_3}", var.get()), 355, 400)
    Frame_class.gen_button_fs("삭제", lambda: btftn.delete_N_listbox(Frame_class, N_List, user_id), 415, 400)
    
    
    
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
    tab_class.insert_label_entry(st_ph_var, "학생 연락처", 193, 10, 285, 10, 12, 27)
    tab_class.insert_label_entry(pa_ph_var, "학부모 연락처", 193, 35, 285, 35, 12, 27)
    tab_class.insert_label_entry(email_var, "e-mail", 226, 60, 285, 60, 7, 27)
    tab_class.insert_label_text("주소", 240, 85, 285, 85, 7, 27, 3)
    tab_class.insert_label_text("특이사항", 10, 145, 15, 170, 7, 66, 10)
    
    tab_class.gen_button_fs("입력", empty_function, 440, 315)

    
    
def info_class(tab):
    
    tab_class = bftn.window_set(tab)
    
    course_var = tk.StringVar()
    class_day_var = tk.StringVar()
    day1_var = tk.StringVar()
    day2_var = tk.StringVar()
    day3_var = tk.StringVar()
    day1_start_var = tk.StringVar()
    day1_end_var = tk.StringVar()
    day2_start_var = tk.StringVar()
    day2_end_var = tk.StringVar()
    day3_start_var = tk.StringVar()
    day3_end_var = tk.StringVar()
    
    main_book_var = tk.StringVar()
    main_start_date_var = tk.StringVar()
    main_end_date_var = tk.StringVar()
    sub_book_var = tk.StringVar()
    sub_start_date_var = tk.StringVar()
    sub_end_date_var = tk.StringVar()
    text_var = tk.StringVar()
    
    
    
    tab_class.gen_label_rely("● 수업 요일/시간", 10, 0.03)
    tab_class.insert_label_entry(course_var, "과정", 55, 40, 30, 40, E_width=6)
    tab_class.insert_label_entry(class_day_var, "요일", 165, 40, 125, 40, E_width=8)
    tab_class.gen_entry(day1_var, 30, 65, 3)
    tab_class.gen_label(":", 60, 65)
    tab_class.gen_entry(day1_start_var, 75, 65, 8)
    tab_class.gen_label("~", 140, 65)
    tab_class.gen_entry(day1_end_var, 160, 65, 8)
    
    tab_class.gen_entry(day2_var, 30, 90, 3)
    tab_class.gen_label(":", 60, 90)
    tab_class.gen_entry(day2_start_var, 75, 90, 8)
    tab_class.gen_label("~", 140, 90)
    tab_class.gen_entry(day2_end_var, 160, 90, 8)
    
    tab_class.gen_entry(day3_var, 30, 115, 3)
    tab_class.gen_label(":", 60, 115)
    tab_class.gen_entry(day3_start_var, 75, 115, 8)
    tab_class.gen_label("~", 140, 115)
    tab_class.gen_entry(day3_end_var, 160, 115, 8)
    
    
    tab_class.gen_label_rely("● 특이사항", 230, 0.03)
    tab_class.gen_textbox(250, 40, 32, 10)
    
    
    tab_class.gen_label_rely("● 진행중인 교재", 10, 0.5)
    tab_class.insert_label_entry(main_book_var, "주 교재", 10, 200, 70, 200, E_width=19)
    tab_class.insert_label_entry(main_start_date_var, "시작일", 210, 200, 270, 200, E_width=10)
    tab_class.insert_label_entry(main_end_date_var, "종료일", 345, 200, 405, 200, E_width=10)
    tab_class.insert_label_entry(sub_book_var, "부 교재", 10, 225, 70, 225, E_width=19)
    tab_class.insert_label_entry(sub_start_date_var, "시작일", 210, 225, 270, 225, E_width=10)
    tab_class.insert_label_entry(sub_end_date_var, "종료일", 345, 225, 405, 225, E_width=10)
    tab_class.insert_label_entry(text_var, "특이사항", 10, 250, 70, 250, E_width=58)
    
    tab_class.gen_button("주교재 시작", empty_function, 70, 280)
    tab_class.gen_button("부교재 시작", empty_function, 159, 280)
    tab_class.gen_button("주교재 종료", empty_function, 250, 280)
    tab_class.gen_button("부교재 종료", empty_function, 339, 280)
    tab_class.gen_button_bs("완료 항목으로 이동", empty_function, 22, 1, 70, 310)
    tab_class.gen_button_bs("완료된 교재", empty_function, 22, 1, 250, 310)
    tab_class.gen_button_bs("입력", empty_function, 6, 3, 428, 280)
    
    
    
def info_consult(tab):
    
    tab_class = bftn.window_set(tab)
    
    subject_var = tk.StringVar()
    date_var = tk.StringVar()
    
    # db로부터 상담일자 받아와서 콤보박스 옵션 만들도록...
    option = ["23-11-14"]
    tab_class.insert_label_entry(subject_var, "상담주제", 10, 10, 75, 10, 7, 25)
    tab_class.insert_label_entry(date_var, "상담일자", 283, 10, 348, 10, 7, 18)
    tab_class.insert_label_text("상담내용", 10, 40, 15, 65, 7, 66, 17)
    tab_class.gen_combobox(option, 12, 15, 305)
    
    tab_class.gen_button_fs("조회", empty_function, 256, 305)
    tab_class.gen_button_fs("수정", empty_function, 316, 305)
    tab_class.gen_button_fs("삭제", empty_function, 376, 305)
    tab_class.gen_button_fs("입력", empty_function, 436, 305)
    

    
def info_exam(tab):
    
    tab_class = bftn.window_set(tab)
    
    data_var = tk.StringVar()
    type_var = tk.StringVar()
    range_var = tk.StringVar()
    score_var = tk.StringVar()
    
    option = ["전체", "중간고사"]
    
    tab_class.gen_label("● 시험기록", 10, 10)
    tab_class.gen_label("날짜", 30, 35)
    Date_List = tab_class.gen_listbox_bs(15, 0.20, 8, 10)
    tab_class.gen_label("시험종류", 115, 20)
    tab_class.gen_combobox(option, 12, 90, 45)
    Type_List = tab_class.gen_listbox_bs(90, 0.20, 15, 10)
    tab_class.gen_label("시험범위", 285, 35)
    Range_List = tab_class.gen_listbox_bs(215, 0.20, 28, 10)
    tab_class.gen_label("점수", 443, 35)
    Score_List = tab_class.gen_listbox_bs(432, 0.20, 7, 10)
    
    tab_class.gen_entry(data_var, 15, 240, 8)
    tab_class.gen_entry(type_var, 90, 240, 15)
    tab_class.gen_entry(range_var, 215, 240, 28)
    tab_class.gen_entry(score_var, 432, 240, 7)
    
    tab_class.gen_button_bs("반 별 일괄입력", empty_function, 15, 2, 15, 290)
    tab_class.gen_button_fs("수정", empty_function, 316, 305)
    tab_class.gen_button_fs("삭제", empty_function, 376, 305)
    tab_class.gen_button_fs("입력", empty_function, 436, 305)

    
    
    
    Date_List.insert(tk.END, "23-11-14")
    Type_List.insert(tk.END, "2-1 단원테스트")
    Range_List.insert(tk.END, "순환소수 ~ 여러 가지 방정식")
    Score_List.insert(tk.END, "100")
    
    
    
    
    
def empty_function():
    a=1
    

    