import pymysql
from datetime import datetime   

import config_set as con
import base_function as bftn
import account_data as acc


# db_conn_config = con.config

def add_T_listbox(Frame_class, T_List, T_entry, Columns, Values):

    if Values != "":
        sql_set = bftn.mysql_set(con.config)
        sql_set.insert_query_str(Columns, Values)
        bftn.clear(T_entry)
        bftn.show_list_box(T_List, f"{con.column[0]}", f"{con.column[0]}")
    else:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "내용을 입력해주세요.")
        
        
        
def modify_T_listbox(Frame_class, T_List, var):
    
    selected_data_c = bftn.get_selectitem(Frame_class, T_List, "선생님을 선택해 주세요.")

    if selected_data_c == False:
        return 0
    else:
        sub_wd = Frame_class.sub_wd()
        sub_wd_class = bftn.window_set(sub_wd)
        sub_wd_class.set_title("선생님 이름 변경")
        sub_wd_class.set_size("195x110")
        sub_wd_class.gen_label("변경할 내용을 입력해 주세요.", 15, 10)
        modify_entry = sub_wd_class.gen_entry(var, 18, 40, 22)
        bftn.clear(modify_entry)
        sub_wd_class.gen_button("확인", lambda: sub_command_6(sub_wd_class, T_List, modify_entry, selected_data_c, f"{con.column[0]}"), 45, 70)
        sub_wd_class.gen_button("취소", sub_wd_class.clear_wd, 115, 70)
        
        
def sub_command_6(sub_wd_class, T_List, modify_entry, selected_data_c, modify_column):
    
    sql_set = bftn.mysql_set(con.config)

    new_data = modify_entry.get()
    cond = f"{modify_column} = '{selected_data_c}'"
    update_data = f"{modify_column} = '{new_data}'"

    sql_set.update_query_value(update_data, cond)

    conditions = f"{con.column[0]} IS NOT NULL"
    bftn.clear(T_List)
    bftn.show_list_box_cond(T_List, f"{con.column[0]}", conditions, f"{con.column[0]}")

    sub_wd_class.clear_wd()
        
                
        
def delete_T_listbox(Frame_class, T_List):
    
    sql_set = bftn.mysql_set(con.config)
    selected_data_t = bftn.get_selectitem(Frame_class, T_List, "내용을 선택해 주세요.")
        
    if selected_data_t == False:
        return 0
    else:
        sub_wd = Frame_class.sub_wd()
        sub_wd_class = bftn.window_set(sub_wd)
        sub_wd_class.set_title("주의")
        sub_wd_class.set_size(con.war_box_size)
        sub_wd_class.gen_label("삭제하시겠습니까?", 45, 10)
        sub_wd_class.gen_button("확인", lambda: sub_command_1(sub_wd_class, sql_set, T_List, selected_data_t, f"{con.column[0]}"), 45, 40)
        sub_wd_class.gen_button("취소", sub_wd_class.clear_wd, 115, 40)

        
def sub_command_1(sub_wd_class, sql_set, List, select_data, list_name):
    sub_wd_class.clear_wd()
    conditions_c = f"{list_name} = '{select_data}'"
    sql_set.delete_query_cond(conditions_c)
    bftn.show_list_box(List, list_name, list_name)
    
    
    
    
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
            bftn.show_list_box_cond(C_List, f"{con.column[1]}", conditions, con.column[1])
    else:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "내용을 입력해주세요.")

    
def lookup_C_listbox(Frame_class, C_List, T_List, N_List):
    
    selected_data = bftn.get_selectitem(Frame_class, T_List, "선생님 항목을 선택해주세요.")
    
    if selected_data == False:
        return 0
    else:
        conditions = f"{con.column[1]} IS NOT NULL AND {con.column[0]} = '{selected_data}'"
        bftn.clear(N_List)
        bftn.show_list_box_cond(C_List, f"{con.column[1]}", conditions, f"{con.column[1]}")


def modify_C_listbox(Frame_class, C_List, user_id, var):
    sql_set = bftn.mysql_set(con.config)
    selected_data = bftn.get_selectitem(Frame_class, C_List, "반을 선택해 주세요.")
        
    conditions = f"{con.column[1]} = '{selected_data}'"
    res = sql_set.select_query(f"{con.column[0]}", conditions)
    
    authority = bftn.authority_check(res, acc.acc_to_tname[user_id.get()])

    if selected_data == False:
        return 0
    elif authority == False:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "권한이 없습니다.")
    else:
        sub_wd = Frame_class.sub_wd()
        sub_wd_class = bftn.window_set(sub_wd)
        sub_wd_class.set_title("반 이름 변경")
        sub_wd_class.set_size("195x110")
        sub_wd_class.gen_label("변경할 내용을 입력해 주세요.", 15, 10)
        modify_entry = sub_wd_class.gen_entry(var, 18, 40, 22)
        bftn.clear(modify_entry)
        sub_wd_class.gen_button("확인", lambda: sub_command_5(sub_wd_class, C_List, modify_entry, selected_data, f"{con.column[1]}", user_id), 45, 70)
        sub_wd_class.gen_button("취소", sub_wd_class.clear_wd, 115, 70)


def sub_command_5(sub_wd_class, List, modify_entry, selected_data, modify_column, user_id):
    
    sql_set = bftn.mysql_set(con.config)

    new_data = modify_entry.get()
    cond = f"{con.column[0]} = '{acc.acc_to_tname[user_id.get()]}' AND {modify_column} = '{selected_data}'"
    update_data = f"{modify_column} = '{new_data}'"

    sql_set.update_query_value(update_data, cond)

    conditions = f"{modify_column} IS NOT NULL AND {con.column[0]} = '{acc.acc_to_tname[user_id.get()]}'"
    bftn.clear(List)
    bftn.show_list_box_cond(List, f"{modify_column}", conditions, f"{modify_column}")

    sub_wd_class.clear_wd()


def delete_C_listbox(Frame_class, C_List, user_id):
    
    sql_set = bftn.mysql_set(con.config)
    selected_data_c = bftn.get_selectitem(Frame_class, C_List, "반을 선택해 주세요.")
        
    conditions = f"{con.column[1]} = '{selected_data_c}'"
    res = sql_set.select_query(f"{con.column[0]}", conditions)
    
    authority = bftn.authority_check(res, acc.acc_to_tname[user_id.get()])
        
    if selected_data_c == False:
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
        sub_wd_class.gen_button("확인", lambda: sub_command_2(sub_wd_class, sql_set, C_List, selected_data_c, f"{con.column[1]}", user_id), 45, 40)
        sub_wd_class.gen_button("취소", sub_wd_class.clear_wd, 115, 40)
                
        
def sub_command_2(sub_wd_class, sql_set, List, select_data, Columns, user_id):
    sub_wd_class.clear_wd()
    conditions_c = f"{Columns} = '{select_data}'"
    conditions_t = f"{Columns} IS NOT NULL AND {con.column[0]} = '{acc.acc_to_tname[user_id.get()]}'"
    sql_set.delete_query_cond(conditions_c)
    bftn.show_list_box_cond(List, Columns, conditions_t, Columns)
    
    
    
    
def add_N_listbox(Frame_class, N_List, N_entry, C_List, user_id, Columns, Values):
    
    sql_set = bftn.mysql_set(con.config)
    
    conditions = f"{con.column[1]} IS NOT NULL AND {con.column[0]} = '{acc.acc_to_tname[user_id.get()]}'"
    res = sql_set.select_query_distinct_cond(f"{con.column[1]}", conditions)
    authority = bftn.authority_check(res, con.selected_class_name)
    
    conditions = f"{con.column[2]} IS NOT NULL"
    res = sql_set.select_query_distinct_cond(f"{con.column[2]}", conditions)
    name_overlap = bftn.authority_check(res, N_entry.get())
    
    if con.selected_class_name == False:
        return 0
    elif authority == False:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "권한이 없습니다.")
    elif name_overlap == True:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "이름이 중복됩니다.")
    else:
        if Values != "":
            query_str = bftn.str_combine(bftn.str_combine(acc.acc_to_tname[user_id.get()], con.selected_class_name), Values)
            sql_set.insert_query_str(Columns, query_str)
            conditions = f"{con.column[2]} IS NOT NULL AND {con.column[1]} = '{con.selected_class_name}'"
            bftn.clear(N_entry)
            bftn.show_list_box_cond(N_List, f"{con.column[2]}", conditions, f"{con.column[2]}")
        else:
            sub_wd = Frame_class.sub_wd()
            bftn.Error_Box(sub_wd, "내용을 입력해주세요.")
            
            
def lookup_N_listbox(Frame_class, C_List, N_List):
    
    con.selected_class_name = bftn.get_selectitem(Frame_class, C_List, "반을 선택해주세요.")
    if con.selected_class_name == False:
        return 0
    else:
        conditions = f"{con.column[2]} IS NOT NULL AND {con.column[1]} = '{con.selected_class_name}'"
        bftn.show_list_box_cond(N_List, f"{con.column[2]}", conditions, f"{con.column[2]}")
        
        
def modify_N_listbox(Frame_class, N_List, user_id, var):
    sql_set = bftn.mysql_set(con.config)
    selected_data = bftn.get_selectitem(Frame_class, N_List, "학생을 선택해 주세요.")
        
    conditions = f"{con.column[2]} = '{selected_data}'"
    res = sql_set.select_query(f"{con.column[0]}", conditions)
    
    authority = bftn.authority_check(res, acc.acc_to_tname[user_id.get()])

    if selected_data == False:
        return 0
    elif authority == False:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "권한이 없습니다.")
    else:
        sub_wd = Frame_class.sub_wd()
        sub_wd_class = bftn.window_set(sub_wd)
        sub_wd_class.set_title("학생 이름 변경")
        sub_wd_class.set_size("195x110")
        sub_wd_class.gen_label("변경할 내용을 입력해 주세요.", 15, 10)
        modify_entry = sub_wd_class.gen_entry(var, 18, 40, 22)
        bftn.clear(modify_entry)
        sub_wd_class.gen_button("확인", lambda: sub_command_7(sub_wd_class, N_List, modify_entry, selected_data, f"{con.column[2]}", user_id), 45, 70)
        sub_wd_class.gen_button("취소", sub_wd_class.clear_wd, 115, 70)
        
        
def sub_command_7(sub_wd_class, List, modify_entry, selected_data, modify_column, user_id):
    
    sql_set = bftn.mysql_set(con.config)

    new_data = modify_entry.get()
    cond = f"{con.column[0]} = '{acc.acc_to_tname[user_id.get()]}' AND {modify_column} = '{selected_data}'"
    update_data = f"{modify_column} = '{new_data}'"

    sql_set.update_query_value(update_data, cond)

    conditions = f"{modify_column} IS NOT NULL AND {con.column[1]} = '{con.selected_class_name}' AND {con.column[0]} = '{acc.acc_to_tname[user_id.get()]}'"
    bftn.clear(List)
    bftn.show_list_box_cond(List, f"{modify_column}", conditions, f"{modify_column}")

    sub_wd_class.clear_wd()
        
        
        
def delete_N_listbox(Frame_class, N_List, user_id):
    
    sql_set = bftn.mysql_set(con.config)
    selected_data_n = bftn.get_selectitem(Frame_class, N_List, "학생을 선택해 주세요.")
        
    conditions = f"{con.column[2]} = '{selected_data_n}'"
    res = sql_set.select_query(f"{con.column[0]}, {con.column[1]}", conditions)

    authority = bftn.authority_check(res, acc.acc_to_tname[user_id.get()])
        
    if selected_data_n == False:
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
        sub_wd_class.gen_button("확인", lambda: sub_command_3(sub_wd_class, sql_set, N_List, selected_data_n, f"{con.column[2]}", res[0][1]), 45, 40)
        sub_wd_class.gen_button("취소", sub_wd_class.clear_wd, 115, 40)
        
    
def sub_command_3(sub_wd_class, sql_set, List, select_data, Columns, class_name):
    sub_wd_class.clear_wd()
    conditions_n = f"{Columns} = '{select_data}'"
    conditions_c = f"{Columns} IS NOT NULL AND {con.column[1]} = '{class_name}'"
    sql_set.delete_query_cond(conditions_n)
    bftn.show_list_box_cond(List, Columns, conditions_c, Columns)
    
    
    
def transfer_N_listbox(Frame_class, user_id, N_List):
    
    selected_st_name = bftn.get_selectitem(Frame_class, N_List, "학생을 선택해주세요.")

    sql_set = bftn.mysql_set(con.config)
    
    conditions = f"{con.column[0]} = '{acc.acc_to_tname[user_id.get()]}'"
    res = sql_set.select_query_distinct_cond(f"{con.column[2]}", conditions)
    
    authority = bftn.authority_check(res, selected_st_name)
    
    if selected_st_name == False:
        return 0
    elif authority == False:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "권한이 없습니다.")
    else:
        conditions = f"{con.column[1]} IS NOT NULL"
        T_list_res = sql_set.select_order_query_distinct(f"{con.column[0]}", f"{con.column[0]}")
        T_list_option = []
        for row in T_list_res:
            T_list_option.append(row)
        
        C_list_res = sql_set.select_order_query_distinct_cond(f"{con.column[1]}", conditions, con.column[1])
        C_list_option = []
        for row in C_list_res:
            C_list_option.append(row)
        
        sub_wd = Frame_class.sub_wd()
        sub_wd_class = bftn.window_set(sub_wd)
        sub_wd_class.set_title("반 이동")
        sub_wd_class.set_size("285x120")
        
        sub_wd_class.gen_label("새로운 선생님과 반을 선택해주세요.", 27, 10)
        T_list_cbox = sub_wd_class.gen_combobox(T_list_option, 10, 30, 40)
        C_list_cbox = sub_wd_class.gen_combobox(C_list_option, 10, 160, 40)
        sub_wd_class.gen_button("확인", lambda: student_transfer(sub_wd_class, N_List, selected_st_name, T_list_cbox, C_list_cbox), 87, 75)
        sub_wd_class.gen_button("취소", sub_wd_class.clear_wd, 160, 75)
    
    
    
def student_transfer(sub_wd_class, N_List, st_name, T_list_cbox, C_list_cbox):
    
    selected_T = T_list_cbox.get()
    selected_C = C_list_cbox.get()
    
    sql_set = bftn.mysql_set(con.config)
    
    conditions = f"{con.column[0]} = '{selected_T}'"
    C_list_res = sql_set.select_query_distinct_cond(f"{con.column[1]}", conditions)
    
    authority = bftn.authority_check(C_list_res, selected_C)
    
    if authority == False:
        sub_wd = sub_wd_class.sub_wd()
        bftn.Error_Box(sub_wd, "선택한 선생님에게 존재하지 않는 반입니다.")
    else:
        cond = f"{con.column[2]} = '{st_name}'"
        update_data = f"{con.column[0]} = '{selected_T}', {con.column[1]} = '{selected_C}'"
        sql_set.update_query_value(update_data, cond)
        conditions = f"{con.column[2]} IS NOT NULL AND {con.column[1]} = '{con.selected_class_name}'"
        bftn.show_list_box_cond(N_List, f"{con.column[2]}", conditions, f"{con.column[2]}")
        sub_wd_class.clear_wd()
        
    
def lookup_info(Frame_class, N_List, student_info, consult_content, consult_date_cbox, exam_type_cbox):
    
    con.selected_st_name = bftn.get_selectitem(Frame_class, N_List, "학생을 선택해주세요.")
    if con.selected_st_name == False:
        return 0
    else:
        conditions = f"{con.column[2]} = '{con.selected_st_name}'"
        consult_content.clear()
        bftn.show_info_cond(student_info, conditions)
        bftn.combobox_list_update(con.selected_st_name, consult_date_cbox, exam_type_cbox,
                                  con.consult_column[1], con.consult_column[2], con.consult_column[2])
        consult_date_cbox.set("")
        exam_type_cbox.set("")
    
    
def add_basic_info(Frame_class, user_id, student_info):
    
    sql_set = bftn.mysql_set(con.config)
    # con.selected_data = bftn.get_selectitem(Frame_class, N_List, "학생을 선택해주세요.")
    
    conditions = f"{con.column[0]} = '{acc.acc_to_tname[user_id.get()]}'"
    res = sql_set.select_query_distinct_cond(f"{con.column[2]}", conditions)
    
    authority = bftn.authority_check(res, con.selected_st_name)
    
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
    
    if con.selected_st_name == False:
        return 0
    elif authority == False:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "권한이 없습니다.")
    else:
        if update_data != []:
            cond = f"{con.column[2]} = '{con.selected_st_name}'"
            sql_set.update_query_value(bftn.list_to_str(update_data), cond)
        else:
            sub_wd = Frame_class.sub_wd()
            bftn.Error_Box(sub_wd, "내용을 입력해주세요.")
    
    
    
def add_class_info(Frame_class, user_id, student_info):
    
    sql_set = bftn.mysql_set(con.config)
    # con.selected_data = bftn.get_selectitem(Frame_class, N_List, "학생을 선택해주세요.")
    
    conditions = f"{con.column[0]} = '{acc.acc_to_tname[user_id.get()]}'"
    res = sql_set.select_query_distinct_cond(f"{con.column[2]}", conditions)
    
    authority = bftn.authority_check(res, con.selected_st_name)
    
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
    
    if con.selected_st_name == False:
        return 0
    elif authority == False:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "권한이 없습니다.")
    else:
        if update_data != []:
            cond = f"{con.column[2]} = '{con.selected_st_name}'"
            sql_set.update_query_value(bftn.list_to_str(update_data), cond)
        else:
            sub_wd = Frame_class.sub_wd()
            bftn.Error_Box(sub_wd, "내용을 입력해주세요.")
            
      

def add_consult_info(Frame_class, user_id, consult_content, consult_date_cbox):
    
    sql_set = bftn.mysql_set(con.config)
    conditions = f"{con.column[0]} = '{acc.acc_to_tname[user_id.get()]}'"
    res = sql_set.select_query_distinct_cond(f"{con.column[2]}", conditions)
    
    authority = bftn.authority_check(res, con.selected_st_name)
    
    conditions = f"{con.consult_column[1]} = '{con.selected_st_name}'"    
    res = sql_set.select_query_distinct_cond(f"{con.consult_column[2]}", conditions, con.consult_table_name)
    
    res_date = []
    for val in res:
        res_date.append(val[0].strftime("%Y-%m-%d"))
        
    if consult_content.date_var.get() == "":
        consult_date = bftn.today()
    else:
        consult_date = consult_content.date_var.get()
        
    date_overlap = bftn.authority_check_val(res_date, consult_date)

    content_var = bftn.get_text(consult_content.content)
    Columns = f"{con.consult_column[0]}, {con.consult_column[1]}, {con.consult_column[2]}, {con.consult_column[3]}, {con.consult_column[4]}"
    
    if con.selected_st_name == False:
        return 0
    elif authority == False:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "권한이 없습니다.")
    elif date_overlap == True:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "상담기록이 존재합니다.")
    else:
        if consult_content.subject_var.get() != "":
            if consult_content.date_var.get() == "":
                query_str = f"{acc.acc_to_tname[user_id.get()]}', '{con.selected_st_name}', '{bftn.today()}', '{consult_content.subject_var.get()}', '{content_var}"
                sql_set.insert_query_str(Columns, query_str, con.consult_table_name)
                bftn.combobox_list_update(con.selected_st_name, consult_date_cbox, 
                                          con.consult_column[1], con.consult_column[2], con.consult_column[2])
            else:
                query_str = f"{acc.acc_to_tname[user_id.get()]}', '{con.selected_st_name}', '{consult_content.date_var.get()}', '{consult_content.subject_var.get()}', '{content_var}"
                sql_set.insert_query_str(Columns, query_str, con.consult_table_name)
                bftn.combobox_list_update(con.selected_st_name, consult_date_cbox, 
                                          con.consult_column[1], con.consult_column[2], con.consult_column[2])
        else:
            sub_wd = Frame_class.sub_wd()
            bftn.Error_Box(sub_wd, "내용을 입력해주세요.")
            
            
            
def lookup_consult_info(Frame_class, consult_content, consult_date_cbox):
        
    con.selected_consult_date = consult_date_cbox.get()
    if con.selected_consult_date == "":
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "날짜를 선택해주세요.")
    else:
        conditions = f"{con.consult_column[1]} = '{con.selected_st_name}' AND {con.consult_column[2]} = '{con.selected_consult_date}'"
        consult_content.clear()
        bftn.show_consult_info_cond(consult_content, conditions)
    

    
def modify_consult_info(Frame_class, consult_content, consult_date_cbox, user_id):
    
    sql_set = bftn.mysql_set(con.config)
    
    _, date, _ = consult_content.get()
    
    conditions = f"{con.consult_column[1]} = '{con.selected_st_name}'"
    res = sql_set.select_query(f"{con.consult_column[0]}, {con.consult_column[2]}", conditions, con.consult_table_name)
    
    if f"{con.selected_consult_date}" != f"{date}":
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "상담일은 변경할 수 없습니다.")
    else:
        authority = bftn.authority_check_tuple(res, acc.acc_to_tname[user_id.get()], date)
        if authority == False:
            sub_wd = Frame_class.sub_wd()
            bftn.Error_Box(sub_wd, "권한이 없습니다.")
        else:
            sub_wd = Frame_class.sub_wd()
            sub_wd_class = bftn.window_set(sub_wd)
            sub_wd_class.set_title("주의")
            sub_wd_class.set_size(con.war_box_size)
            sub_wd_class.gen_label("변경하시겠습니까?", 45, 10)
            sub_wd_class.gen_button("확인", lambda: sub_command_8(sub_wd_class, consult_content, consult_date_cbox), 45, 40)
            sub_wd_class.gen_button("취소", sub_wd_class.clear_wd, 115, 40)
        

    
def sub_command_8(sub_wd_class, consult_content, consult_date_cbox):
    
    sql_set = bftn.mysql_set(con.config)
    
    subject, date, content = consult_content.get()    
    
    cond = f"{con.consult_column[1]} = '{con.selected_st_name}' AND {con.consult_column[2]} = '{date}'"
    update_data = f"{con.consult_column[3]} = '{subject}', {con.consult_column[4]} = '{content}'"
    sql_set.update_query_value(update_data, cond, con.consult_table_name)
    
    sub_wd_class.clear_wd()
    
    
    
def delete_consult_info(Frame_class, consult_content, consult_date_cbox, user_id):
    
    sql_set = bftn.mysql_set(con.config)
    selected_date = consult_date_cbox.get()

    conditions = f"{con.consult_column[1]} = '{con.selected_st_name}'"
    res = sql_set.select_query(f"{con.consult_column[0]}", conditions, con.consult_table_name)

    authority = bftn.authority_check(res, acc.acc_to_tname[user_id.get()])
        
    if selected_date == False:
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
        sub_wd_class.gen_button("확인", lambda: sub_command_4(sub_wd_class, consult_content, consult_date_cbox, selected_date), 45, 40)
        sub_wd_class.gen_button("취소", sub_wd_class.clear_wd, 115, 40)
        
    
    
def sub_command_4(sub_wd_class, consult_content, consult_date_cbox, selected_date):
    
    sql_set = bftn.mysql_set(con.config)
    
    sub_wd_class.clear_wd()
    conditions = f"{con.consult_column[1]} = '{con.selected_st_name}' AND {con.consult_column[2]} = '{selected_date}'"
    sql_set.delete_query_cond(conditions, con.consult_table_name)
    consult_content.clear()
    bftn.combobox_list_update(con.selected_st_name, consult_date_cbox, 
                              con.consult_column[1], con.consult_column[2], con.consult_column[2] )



def add_exam_info(Frame_class, tree, exam_content, user_id):
    
    sql_set = bftn.mysql_set(con.config)
    conditions = f"{con.column[0]} = '{acc.acc_to_tname[user_id.get()]}'"
    res = sql_set.select_query_distinct_cond(f"{con.column[2]}", conditions)

    authority = bftn.authority_check(res, con.selected_st_name)

    Columns = f"{con.exam_column[0]}, {con.exam_column[1]}, {con.exam_column[2]}, {con.exam_column[3]}, {con.exam_column[4]}, {con.exam_column[5]}"
    
    if con.selected_st_name == False:
        return 0
    elif authority == False:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "권한이 없습니다.")
    else:
        if exam_content.exam_type_var.get() != "" and exam_content.exam_range_var.get() != "" and exam_content.score_var.get() != "":
            if exam_content.date_var.get() == "":
                query_str = f"{acc.acc_to_tname[user_id.get()]}', '{con.selected_st_name}', '{bftn.today()}', '{exam_content.exam_type_var.get()}', '{exam_content.exam_range_var.get()}', '{exam_content.score_var.get()}"
                sql_set.insert_query_str(Columns, query_str, con.exam_table_name)
                exam_content.clear()
                tree.delete(*tree.get_children())
                all_exam_content = bftn.get_all_exam_list(con.selected_st_name)
                for content in all_exam_content:
                    tree.insert('', 'end', values=content)
            else:
                query_str = f"{acc.acc_to_tname[user_id.get()]}', '{con.selected_st_name}', '{exam_content.date_var.get()}', '{exam_content.exam_type_var.get()}', '{exam_content.exam_range_var.get()}', '{exam_content.score_var.get()}"
                sql_set.insert_query_str(Columns, query_str, con.exam_table_name)
                exam_content.clear()
                tree.delete(*tree.get_children())
                all_exam_content = bftn.get_all_exam_list(con.selected_st_name)
                for content in all_exam_content:
                    tree.insert('', 'end', values=content)
        else:
            sub_wd = Frame_class.sub_wd()
            bftn.Error_Box(sub_wd, "내용을 입력해주세요.")
            
            
            
def lookup_exam_info(Frame_class, exam_type_cbox, tree):

    tree.delete(*tree.get_children())
    
    selected_date = exam_type_cbox.get()
    if selected_date == "":
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "시험종류를 선택해주세요.")
    else:
        all_exam_content = bftn.get_all_exam_list(con.selected_st_name)
        if exam_type_cbox.get() == "전체":
            for content in all_exam_content:
                tree.insert('', 'end', values=content)
        else:
            for content in all_exam_content:
                if content[2] == selected_date:
                    tree.insert('', 'end', values=content)
                    
                    
                    
def modify_exam_info(Frame_class, exam_content, tree, user_id):
    
    sql_set = bftn.mysql_set(con.config)
    
    selected_date_id = tree.selection()  
    selected_data = tree.item(selected_date_id)['values']
        
    conditions = f"{con.exam_column[6]} = '{selected_data[0]}'"
    res = sql_set.select_query_distinct_cond("*", conditions, con.exam_table_name)
    authority = bftn.authority_check(res, acc.acc_to_tname[user_id.get()])
    
    if selected_date_id == ():
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "내용을 선택해주세요.")
    else:
        if authority == False:
            sub_wd = Frame_class.sub_wd()
            bftn.Error_Box(sub_wd, "권한이 없습니다.")
        else:
            sub_wd = Frame_class.sub_wd()
            sub_wd_class = bftn.window_set(sub_wd)
            sub_wd_class.set_title("주의")
            sub_wd_class.set_size(con.war_box_size)
            sub_wd_class.gen_label("변경하시겠습니까?", 45, 10)
            sub_wd_class.gen_button("확인", lambda: sub_command_10(sub_wd_class, exam_content, selected_data[0]), 45, 40)
            sub_wd_class.gen_button("취소", sub_wd_class.clear_wd, 115, 40)
        


def sub_command_10(sub_wd_class, exam_content, exam_number):
    
    sql_set = bftn.mysql_set(con.config)
    
    cond = f"{con.exam_column[6]} = {exam_number}"
    update_data = f"{con.exam_column[2]} = '{exam_content.date_var.get()}', {con.exam_column[3]} = '{exam_content.exam_type_var.get()}', {con.exam_column[4]} = '{exam_content.exam_range_var.get()}', {con.exam_column[5]} = {exam_content.score_var.get()}"
    sql_set.update_query_value(update_data, cond, con.exam_table_name)
    sub_wd_class.clear_wd()
    
                    
                    
def delete_exam_info(Frame_class, tree, user_id):
    
    sql_set = bftn.mysql_set(con.config)
    selected_date_id = tree.selection()    
        
    if selected_date_id == ():
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "내용을 선택해주세요.")
    else:
        selected_data = tree.item(selected_date_id)['values']
        conditions = f"{con.exam_column[6]} = '{selected_data[0]}'"
        res = sql_set.select_query_distinct_cond(f"{con.exam_column[0]}, {con.exam_column[6]}", conditions, con.exam_table_name)
        authority = bftn.authority_check(res, acc.acc_to_tname[user_id.get()])
        if authority == False:
            sub_wd = Frame_class.sub_wd()
            bftn.Error_Box(sub_wd, "권한이 없습니다.")
        else:
            sub_wd = Frame_class.sub_wd()
            sub_wd_class = bftn.window_set(sub_wd)
            sub_wd_class.set_title("주의")
            sub_wd_class.set_size(con.war_box_size)
            sub_wd_class.gen_label("삭제하시겠습니까?", 45, 10)
            sub_wd_class.gen_button("확인", lambda: sub_command_9(sub_wd_class, tree, selected_date_id), 45, 40)
            sub_wd_class.gen_button("취소", sub_wd_class.clear_wd, 115, 40)
        
        
def sub_command_9(sub_wd_class, tree, selected_date_id):
    
    sql_set = bftn.mysql_set(con.config)
    
    sub_wd_class.clear_wd()
    
    selected_data = tree.item(selected_date_id)['values']
    
    conditions = f"{con.exam_column[6]} = '{selected_data[0]}'"
    sql_set.delete_query_cond(conditions, con.exam_table_name)
    tree.delete(selected_date_id)
    
    
        
def empty_function():
    a=1
    
    
# 완료된 교재 목록 볼때...
def lookup_allexam_info(Frame_class):
        
    sub_wd = Frame_class.sub_wd()
    sub_wd_class = bftn.window_set(sub_wd)
    sub_wd_class.set_title("시험결과 전체보기")
    sub_wd_class.set_size("650x450")
    
    options = ["전체"]
    bftn.get_exam_list(options, con.exam_column[3], con.selected_st_name)
    
    sub_wd_class.gen_label("시험종류 선택", 10, 10)
    exam_type_cbox = sub_wd_class.gen_combobox(options, 12, 10, 35)
    
    sub_wd_class.gen_button_fs("조회", empty_function, 150, 35)
    sub_wd_class.gen_button_fs("수정", empty_function, 215, 35)
    sub_wd_class.gen_button_fs("삭제", empty_function, 280, 35)
    
    exam_columns = ('col 1', 'col 2', 'col 3', 'col 4', 'col 5')
    tree = sub_wd_class.gen_treeview(exam_columns, 10, 80)
    
    tree.heading('col 1', text='번호')
    tree.heading('col 2', text='날짜')
    tree.heading('col 3', text='시험종류')
    tree.heading('col 4', text='시험범위')
    tree.heading('col 5', text='점수')
    
    tree.column('col 1', width=50)
    tree.column('col 2', width=100)
    tree.column('col 3', width=150)
    tree.column('col 4', width=250)
    tree.column('col 5', width=75)
    
    
    all_exam_content = bftn.get_all_exam_list(con.selected_st_name)
    
    for content in all_exam_content:
        tree.insert('', 'end', values=content)
    
    # selected_date = exam_type_cbox.get()
    # if selected_date == "":
    #     sub_wd = Frame_class.sub_wd()
    #     bftn.Error_Box(sub_wd, "시험종류를 선택해주세요.")
    # else:
    #     if exam_type_cbox.get() == "전체":
    #         conditions = f"{con.exam_column[1]} = '{con.selected_st_name}'"
    #     else:
    #         conditions = f"{con.exam_column[1]} = '{con.selected_st_name}' AND {con.exam_column[3]} = '{selected_date}'"