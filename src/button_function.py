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
        bftn.show_list_box(T_List, f"{con.column_1}")
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
        sub_wd_class.gen_button("확인", lambda: sub_command_1(sub_wd_class, sql_set, T_List, select_data_t, f"{con.column_1}"), 45, 40)
        sub_wd_class.gen_button("취소", sub_wd_class.clear_wd, 115, 40)

        
def sub_command_1(sub_wd_class, sql_set, List, select_data, list_name):
    sub_wd_class.clear_wd()
    conditions_c = f"{list_name} = '{select_data}'"
    sql_set.delete_query_cond(conditions_c)
    bftn.show_list_box(List, list_name)
    
    
    
    
def add_C_listbox(Frame_class, C_List, C_entry, user_id, Columns, Values):
    
    sql_set = bftn.mysql_set(con.config)

    conditions = f"{con.column_2} IS NOT NULL"
    res = sql_set.select_query_distinct_cond(f"{con.column_2}", conditions)
    
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
            conditions = f"{con.column_2} IS NOT NULL AND {con.column_1} = '{acc.acc_to_tname[user_id.get()]}'"
            bftn.clear(C_entry)
            bftn.show_list_box_cond(C_List, f"{con.column_2}", conditions)
    else:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "내용을 입력해주세요.")

    
def lookup_C_listbox(Frame_class, C_List, T_List, N_List):
    
    select_data = bftn.get_selectitem(Frame_class, T_List, "선생님 항목을 선택해주세요.")
    
    if select_data == False:
        return 0
    else:
        conditions = f"{con.column_2} IS NOT NULL AND {con.column_1} = '{select_data}'"
        bftn.clear(N_List)
        bftn.show_list_box_cond(C_List, f"{con.column_2}", conditions)
        

def delete_C_listbox(Frame_class, C_List, user_id):
    
    sql_set = bftn.mysql_set(con.config)
    select_data_c = bftn.get_selectitem(Frame_class, C_List, "반을 선택해 주세요.")
        
    conditions = f"{con.column_2} = '{select_data_c}'"
    res = sql_set.select_query(f"{con.column_1}", conditions)
    
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
        sub_wd_class.gen_button("확인", lambda: sub_command_2(sub_wd_class, sql_set, C_List, select_data_c, f"{con.column_2}", user_id), 45, 40)
        sub_wd_class.gen_button("취소", sub_wd_class.clear_wd, 115, 40)
                
        
def sub_command_2(sub_wd_class, sql_set, List, select_data, Columns, user_id):
    sub_wd_class.clear_wd()
    conditions_c = f"{Columns} = '{select_data}'"
    conditions_t = f"{Columns} IS NOT NULL AND {con.column_1} = '{acc.acc_to_tname[user_id.get()]}'"
    sql_set.delete_query_cond(conditions_c)
    bftn.show_list_box_cond(List, Columns, conditions_t)
    
    
    
    
def add_N_listbox(Frame_class, N_List, N_entry, C_List, user_id, Columns, Values):
    
    sql_set = bftn.mysql_set(con.config)
    select_data = bftn.get_selectitem(Frame_class, C_List, "반을 선택해주세요.")
    
    conditions = f"{con.column_2} IS NOT NULL AND {con.column_1} = '{acc.acc_to_tname[user_id.get()]}'"
    res = sql_set.select_query_distinct_cond(f"{con.column_2}", conditions)
    
    authority = bftn.authority_check(res, select_data)
    
    if select_data == False:
        return 0
    elif authority == False:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "권한이 없습니다.")
    else:
        if Values != "":
            query_str = bftn.str_combine(bftn.str_combine(acc.acc_to_tname[user_id.get()], select_data), Values)
            sql_set.insert_query_str(Columns, query_str)
            conditions = f"{con.column_3} IS NOT NULL AND {con.column_2} = '{select_data}'"
            bftn.clear(N_entry)
            bftn.show_list_box_cond(N_List, f"{con.column_3}", conditions)
        else:
            sub_wd = Frame_class.sub_wd()
            bftn.Error_Box(sub_wd, "내용을 입력해주세요.")
            
            
def lookup_N_listbox(Frame_class, C_List, N_List):
    
    select_data = bftn.get_selectitem(Frame_class, C_List, "반을 선택해주세요.")
    if select_data == False:
        return 0
    else:
        conditions = f"{con.column_3} IS NOT NULL AND {con.column_2} = '{select_data}'"
        bftn.show_list_box_cond(N_List, f"{con.column_3}", conditions)
        
        
def delete_N_listbox(Frame_class, N_List, user_id):
    
    sql_set = bftn.mysql_set(con.config)
    select_data_n = bftn.get_selectitem(Frame_class, N_List, "학생을 선택해 주세요.")
        
    conditions = f"{con.column_3} = '{select_data_n}'"
    res = sql_set.select_query(f"{con.column_1}, {con.column_2}", conditions)

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
        sub_wd_class.gen_button("확인", lambda: sub_command_3(sub_wd_class, sql_set, N_List, select_data_n, f"{con.column_3}", res[0][1]), 45, 40)
        sub_wd_class.gen_button("취소", sub_wd_class.clear_wd, 115, 40)
        
    
def sub_command_3(sub_wd_class, sql_set, List, select_data, Columns, class_name):
    sub_wd_class.clear_wd()
    conditions_n = f"{Columns} = '{select_data}'"
    conditions_c = f"{Columns} IS NOT NULL AND {con.column_2} = '{class_name}'"
    sql_set.delete_query_cond(conditions_n)
    bftn.show_list_box_cond(List, Columns, conditions_c)