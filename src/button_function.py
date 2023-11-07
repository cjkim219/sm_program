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
        bftn.show_list_box(T_List, "teacher")
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
        sub_wd_class.gen_button("확인", lambda: sub_command_1(sub_wd_class, sql_set, T_List, select_data_t, "teacher"), 45, 40)
        sub_wd_class.gen_button("취소", sub_wd_class.clear_wd, 115, 40)

        
def sub_command_1(sub_wd_class, sql_set, List, select_data, list_name):
    sub_wd_class.clear_wd()
    conditions_c = f"{list_name} = '{select_data}'"
    sql_set.delete_query_cond(conditions_c)
    bftn.show_list_box(List, list_name)
    
    
def add_C_listbox(Frame_class, C_List, C_entry, T_List, user_id, Columns, Values):
    
    sql_set = bftn.mysql_set(con.config)
    select_data = bftn.get_selectitem(Frame_class, T_List, "선생님 항목을 선택해주세요.")
    if select_data == False:
        return 0
    elif select_data != acc.acc_to_tname[user_id.get()]:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "권한이 없습니다.")
    else:
        ## 반 이름이 중복되는 경우를 체크하여 중복 불가능하게
        if Values != "":
            query_value = bftn.str_combine(select_data, Values)
            conditions = f"class_name IS NOT NULL AND teacher = '{select_data}'"
            sql_set.insert_query_str(Columns, query_value)
            bftn.clear(C_entry)
            bftn.show_list_box_cond(C_List, "class_name", conditions)
        else:
            sub_wd = Frame_class.sub_wd()
            bftn.Error_Box(sub_wd, "내용을 입력해주세요.")

    
def lookup_C_listbox(Frame_class, C_List, T_List):
    
    select_data = bftn.get_selectitem(Frame_class, T_List, "선생님 항목을 선택해주세요.")
    if select_data == False:
        return 0
    else:
        conditions = f"class_name IS NOT NULL AND teacher = '{select_data}'"
        bftn.show_list_box_cond(C_List, "class_name", conditions)
        

def delete_C_listbox(Frame_class, C_List, user_id):
    
    sql_set = bftn.mysql_set(con.config)
    select_data_c = bftn.get_selectitem(Frame_class, C_List, "반을 선택해 주세요.")
        
    if select_data_c == False:
        return 0
    else:
        sub_wd = Frame_class.sub_wd()
        sub_wd_class = bftn.window_set(sub_wd)
        sub_wd_class.set_title("주의")
        sub_wd_class.set_size(con.war_box_size)
        sub_wd_class.gen_label("삭제하시겠습니까?", 45, 10)
        sub_wd_class.gen_button("확인", lambda: sub_command_2(sub_wd_class, sql_set, C_List, select_data_c, "class_name", user_id), 45, 40)
        sub_wd_class.gen_button("취소", sub_wd_class.clear_wd, 115, 40)
                
        
def sub_command_2(sub_wd_class, sql_set, List, select_data, list_name, user_id):
    sub_wd_class.clear_wd()
    conditions_c = f"{list_name} = '{select_data}'"
    conditions_t = f"{list_name} IS NOT NULL AND teacher = '{acc.acc_to_tname[user_id.get()]}'"
    sql_set.delete_query_cond(conditions_c)
    bftn.show_list_box_cond(List, list_name, conditions_t)
    
    
    
def add_N_listbox(Frame_class, N_List, N_entry, C_List, user_id, Columns, Values):
    
    sql_set = bftn.mysql_set(con.config)
    select_data = bftn.get_selectitem(Frame_class, C_List, "반을 선택해주세요.")
    if select_data == False:
        return 0
    
    
    ### 반 리스트를 불러와서 select_data와 비교하여 권한 확인하기.
    elif select_data != acc.acc_to_tname[user_id.get()]:
        sub_wd = Frame_class.sub_wd()
        bftn.Error_Box(sub_wd, "권한이 없습니다.")
    else:
        if Values != "":
            query_value = bftn.str_combine(bftn.str_combine(user_id.get(), select_data), Values)
            conditions = f"name IS NOT NULL AND class_name = '{select_data}'"
            sql_set.insert_query_str(Columns, query_value)
            bftn.clear(N_entry)
            bftn.show_list_box_cond(N_List, "name", conditions)
        else:
            sub_wd = Frame_class.sub_wd()
            bftn.Error_Box(sub_wd, "내용을 입력해주세요.")