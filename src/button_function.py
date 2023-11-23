import pymysql


import config_set as con
import base_function as bftn
import account_data as acc


# db_conn_config = con.config

def add_T_listbox(Frame_class, T_List, T_entry, Columns, Values):

    if Values != "":
        sql_set = bftn.mysql_set(con.config)
        sql_set.insert_query_str(Columns, Values)
        bftn.clear(T_entry)
        bftn.show_list_box(T_List, f"{con.column[0]}")
    else:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "내용을 입력해주세요.")
        
        
def delete_T_listbox(Frame_class, T_List):
    
    sql_set = bftn.mysql_set(con.config)
    select_data_t = bftn.get_selectitem(Frame_class, T_List, "내용을 선택해 주세요.")
        
    if select_data_t == False:
        return 0
    else:
        sub_wd = Frame_class.sub_wd()
        sub_wd_class = bftn.window_set(sub_wd)
        sub_wd_class.set_title("주의")
        sub_wd_class.set_size(con.war_box_size)
        sub_wd_class.gen_label("삭제하시겠습니까?", 45, 10)
        sub_wd_class.gen_button("확인", lambda: sub_command_1(sub_wd_class, sql_set, T_List, select_data_t, f"{con.column[0]}"), 45, 40)
        sub_wd_class.gen_button("취소", sub_wd_class.clear_wd, 115, 40)

        
def sub_command_1(sub_wd_class, sql_set, List, select_data, list_name):
    sub_wd_class.clear_wd()
    conditions_c = f"{list_name} = '{select_data}'"
    sql_set.delete_query_cond(conditions_c)
    bftn.show_list_box(List, list_name)
    
    
    
    
def add_C_listbox(Frame_class, C_List, C_entry, user_id, Columns, Values):
    
    sql_set = bftn.mysql_set(con.config)

    conditions = f"{con.column[1]} IS NOT NULL"
    res = sql_set.select_query_distinct_cond(f"{con.column[1]}", conditions)
    
    overlap = False
    for val in res:
        if val[0] == Values:
            overlap = True
            break
    
    if Values != "":
        if overlap == True:
            sub_wd = Frame_class.sub_wd()
            bftn.Error_Box(sub_wd, "이미 존재하는 반 입니다.")
        else:
            query_str = bftn.str_combine(acc.acc_to_tname[user_id.get()], Values)
            sql_set.insert_query_str(Columns, query_str)
            conditions = f"{con.column[1]} IS NOT NULL AND {con.column[0]} = '{acc.acc_to_tname[user_id.get()]}'"
            bftn.clear(C_entry)
            bftn.show_list_box_cond(C_List, f"{con.column[1]}", conditions)
    else:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "내용을 입력해주세요.")

    
def lookup_C_listbox(Frame_class, C_List, T_List, N_List):
    
    select_data = bftn.get_selectitem(Frame_class, T_List, "선생님 항목을 선택해주세요.")
    
    if select_data == False:
        return 0
    else:
        conditions = f"{con.column[1]} IS NOT NULL AND {con.column[0]} = '{select_data}'"
        bftn.clear(N_List)
        bftn.show_list_box_cond(C_List, f"{con.column[1]}", conditions)
        

def delete_C_listbox(Frame_class, C_List, user_id):
    
    sql_set = bftn.mysql_set(con.config)
    select_data_c = bftn.get_selectitem(Frame_class, C_List, "반을 선택해 주세요.")
        
    conditions = f"{con.column[1]} = '{select_data_c}'"
    res = sql_set.select_query(f"{con.column[0]}", conditions)
    
    authority = bftn.authority_check(res, acc.acc_to_tname[user_id.get()])
        
    if select_data_c == False:
        return 0
    elif authority == False:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "권한이 없습니다.")
    else:
        sub_wd = Frame_class.sub_wd()
        sub_wd_class = bftn.window_set(sub_wd)
        sub_wd_class.set_title("주의")
        sub_wd_class.set_size(con.war_box_size)
        sub_wd_class.gen_label("삭제하시겠습니까?", 45, 10)
        sub_wd_class.gen_button("확인", lambda: sub_command_2(sub_wd_class, sql_set, C_List, select_data_c, f"{con.column[1]}", user_id), 45, 40)
        sub_wd_class.gen_button("취소", sub_wd_class.clear_wd, 115, 40)
                
        
def sub_command_2(sub_wd_class, sql_set, List, select_data, Columns, user_id):
    sub_wd_class.clear_wd()
    conditions_c = f"{Columns} = '{select_data}'"
    conditions_t = f"{Columns} IS NOT NULL AND {con.column[0]} = '{acc.acc_to_tname[user_id.get()]}'"
    sql_set.delete_query_cond(conditions_c)
    bftn.show_list_box_cond(List, Columns, conditions_t)
    
    
    
    
def add_N_listbox(Frame_class, N_List, N_entry, C_List, user_id, Columns, Values):
    
    sql_set = bftn.mysql_set(con.config)
    select_data = bftn.get_selectitem(Frame_class, C_List, "반을 선택해주세요.")
    
    conditions = f"{con.column[1]} IS NOT NULL AND {con.column[0]} = '{acc.acc_to_tname[user_id.get()]}'"
    res = sql_set.select_query_distinct_cond(f"{con.column[1]}", conditions)
    authority = bftn.authority_check(res, select_data)
    
    conditions = f"{con.column[2]} IS NOT NULL"
    res = sql_set.select_query_distinct_cond(f"{con.column[2]}", conditions)
    name_overlap = bftn.authority_check(res, N_entry.get())
    
    if select_data == False:
        return 0
    elif authority == False:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "권한이 없습니다.")
    elif name_overlap == True:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "이름이 중복됩니다.")
    else:
        if Values != "":
            query_str = bftn.str_combine(bftn.str_combine(acc.acc_to_tname[user_id.get()], select_data), Values)
            sql_set.insert_query_str(Columns, query_str)
            conditions = f"{con.column[2]} IS NOT NULL AND {con.column[1]} = '{select_data}'"
            bftn.clear(N_entry)
            bftn.show_list_box_cond(N_List, f"{con.column[2]}", conditions)
        else:
            sub_wd = Frame_class.sub_wd()
            bftn.Error_Box(sub_wd, "내용을 입력해주세요.")
            
            
def lookup_N_listbox(Frame_class, C_List, N_List):
    
    select_data = bftn.get_selectitem(Frame_class, C_List, "반을 선택해주세요.")
    if select_data == False:
        return 0
    else:
        conditions = f"{con.column[2]} IS NOT NULL AND {con.column[1]} = '{select_data}'"
        bftn.show_list_box_cond(N_List, f"{con.column[2]}", conditions)
        
        
def delete_N_listbox(Frame_class, N_List, user_id):
    
    sql_set = bftn.mysql_set(con.config)
    select_data_n = bftn.get_selectitem(Frame_class, N_List, "학생을 선택해 주세요.")
        
    conditions = f"{con.column[2]} = '{select_data_n}'"
    res = sql_set.select_query(f"{con.column[0]}, {con.column[1]}", conditions)

    authority = bftn.authority_check(res, acc.acc_to_tname[user_id.get()])
        
    if select_data_n == False:
        return 0
    elif authority == False:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "권한이 없습니다.")
    else:
        sub_wd = Frame_class.sub_wd()
        sub_wd_class = bftn.window_set(sub_wd)
        sub_wd_class.set_title("주의")
        sub_wd_class.set_size(con.war_box_size)
        sub_wd_class.gen_label("삭제하시겠습니까?", 45, 10)
        sub_wd_class.gen_button("확인", lambda: sub_command_3(sub_wd_class, sql_set, N_List, select_data_n, f"{con.column[2]}", res[0][1]), 45, 40)
        sub_wd_class.gen_button("취소", sub_wd_class.clear_wd, 115, 40)
        
    
def sub_command_3(sub_wd_class, sql_set, List, select_data, Columns, class_name):
    sub_wd_class.clear_wd()
    conditions_n = f"{Columns} = '{select_data}'"
    conditions_c = f"{Columns} IS NOT NULL AND {con.column[1]} = '{class_name}'"
    sql_set.delete_query_cond(conditions_n)
    bftn.show_list_box_cond(List, Columns, conditions_c)
    
    
    
def lookup_info(Frame_class, N_List, student_info, consult_content, consult_date_list):
    
    select_data = bftn.get_selectitem(Frame_class, N_List, "학생을 선택해주세요.")
    if select_data == False:
        return 0
    else:
        conditions = f"{con.column[2]} = '{select_data}'"
        consult_content.clear()
        bftn.show_info_cond(student_info, conditions)
        bftn.combobox_list_update(select_data, consult_date_list, con.consult_column[0], con.consult_column[1])
    
    
    
def add_basic_info(Frame_class, N_List, user_id, student_info):
    
    sql_set = bftn.mysql_set(con.config)
    select_data = bftn.get_selectitem(Frame_class, N_List, "학생을 선택해주세요.")
    
    conditions = f"{con.column[0]} = '{acc.acc_to_tname[user_id.get()]}'"
    res = sql_set.select_query_distinct_cond(f"{con.column[2]}", conditions)
    
    authority = bftn.authority_check(res, select_data)
    
    update_data = []
    
    address_var = bftn.get_text(student_info.address)
    etc_var = bftn.get_text(student_info.etc)
    
    bftn.add_col_val_list(update_data, 3, student_info.age_var.get())
    bftn.add_col_val_list(update_data, 4, student_info.gender_var.get())
    bftn.add_col_val_list(update_data, 5, student_info.school_var.get())
    bftn.add_col_val_list(update_data, 6, student_info.grade_var.get())
    bftn.add_col_val_list(update_data, 7, student_info.birth_var.get())
    bftn.add_col_val_list(update_data, 8, student_info.st_HP_var.get())
    bftn.add_col_val_list(update_data, 9, student_info.pa_HP_var.get())
    bftn.add_col_val_list(update_data, 10, student_info.email_var.get())
    bftn.add_col_val_list(update_data, 11, address_var)
    bftn.add_col_val_list(update_data, 12, etc_var)
    
    if select_data == False:
        return 0
    elif authority == False:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "권한이 없습니다.")
    else:
        if update_data != []:
            cond = f"{con.column[2]} = '{select_data}'"
            sql_set.update_query_value(bftn.list_to_str(update_data), cond)
        else:
            sub_wd = Frame_class.sub_wd()
            bftn.Error_Box(sub_wd, "내용을 입력해주세요.")
    
    
    
def add_class_info(Frame_class, N_List, user_id, student_info):
    
    sql_set = bftn.mysql_set(con.config)
    select_data = bftn.get_selectitem(Frame_class, N_List, "학생을 선택해주세요.")
    
    conditions = f"{con.column[0]} = '{acc.acc_to_tname[user_id.get()]}'"
    res = sql_set.select_query_distinct_cond(f"{con.column[2]}", conditions)
    
    authority = bftn.authority_check(res, select_data)
    
    update_data = []
    
    text1_var = bftn.get_text(student_info.text1)
    
    bftn.add_col_val_list(update_data, 13, student_info.course_var.get())
    bftn.add_col_val_list(update_data, 14, student_info.class_day_var.get())
    bftn.add_col_val_list(update_data, 15, student_info.day1_var.get())
    bftn.add_col_val_list(update_data, 16, student_info.day2_var.get())
    bftn.add_col_val_list(update_data, 17, student_info.day3_var.get())
    bftn.add_col_val_list(update_data, 18, student_info.day1_start_var.get())
    bftn.add_col_val_list(update_data, 19, student_info.day1_end_var.get())
    bftn.add_col_val_list(update_data, 20, student_info.day2_start_var.get())
    bftn.add_col_val_list(update_data, 21, student_info.day2_end_var.get())
    bftn.add_col_val_list(update_data, 22, student_info.day3_start_var.get())
    bftn.add_col_val_list(update_data, 23, student_info.day3_end_var.get())
    
    bftn.add_col_val_list(update_data, 24, student_info.main_book_var.get())
    bftn.add_col_val_list(update_data, 25, student_info.main_start_date_var.get())
    bftn.add_col_val_list(update_data, 26, student_info.main_end_date_var.get())
    bftn.add_col_val_list(update_data, 27, student_info.sub_book_var.get())
    bftn.add_col_val_list(update_data, 28, student_info.sub_start_date_var.get())
    bftn.add_col_val_list(update_data, 29, student_info.sub_end_date_var.get())
    bftn.add_col_val_list(update_data, 30, text1_var)
    bftn.add_col_val_list(update_data, 31, student_info.text2_var.get())
    
    if select_data == False:
        return 0
    elif authority == False:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "권한이 없습니다.")
    else:
        if update_data != []:
            cond = f"{con.column[2]} = '{select_data}'"
            sql_set.update_query_value(bftn.list_to_str(update_data), cond)
        else:
            sub_wd = Frame_class.sub_wd()
            bftn.Error_Box(sub_wd, "내용을 입력해주세요.")
            
            

def add_consult_info(Frame_class, N_List, user_id, consult_content, consult_date_list):
    
    sql_set = bftn.mysql_set(con.config)
    select_data = bftn.get_selectitem(Frame_class, N_List, "학생을 선택해주세요.")
    
    conditions = f"{con.column[0]} = '{acc.acc_to_tname[user_id.get()]}'"
    res = sql_set.select_query_distinct_cond(f"{con.column[2]}", conditions)
    
    authority = bftn.authority_check(res, select_data)
    
    content_var = bftn.get_text(consult_content.content)
    
    Columns = f"{con.consult_column[0]}, {con.consult_column[1]}, {con.consult_column[2]}, {con.consult_column[3]}"
    
    if select_data == False:
        return 0
    elif authority == False:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "권한이 없습니다.")
    else:
        if consult_content.subject_var.get() != "":
            if consult_content.date_var.get() == "":
                query_str = f"{select_data}', '{bftn.today()}', '{consult_content.subject_var.get()}', '{content_var}"
                sql_set.insert_query_str(Columns, query_str, con.consult_table_name)
                bftn.combobox_list_update(select_data, consult_date_list, con.consult_column[0], con.consult_column[1])
            else:
                query_str = f"{select_data}', '{consult_content.date_var.get()}', '{consult_content.subject_var.get()}', '{content_var}"
                sql_set.insert_query_str(Columns, query_str, con.consult_table_name)
                bftn.combobox_list_update(select_data, consult_date_list, con.consult_column[0], con.consult_column[1])
        else:
            sub_wd = Frame_class.sub_wd()
            bftn.Error_Box(sub_wd, "내용을 입력해주세요.")