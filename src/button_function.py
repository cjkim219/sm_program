import pymysql


import config_set as con
import base_function as bftn


# db_conn_config = con.config

def add_T_listbox(Frame_class, T_List, T_Entry, Columns, Values):
    
    sub_wd = Frame_class.sub_wd()
    sub_wd.title("오류")
    
    sql_set = bftn.mysql_set(con.config)
    sql_set.insert_query_str(Columns, Values)
    bftn.clear(T_Entry)
    bftn.show_list_box(T_List, "teacher")
    
    
def add_C_listbox(Frame_class, C_List, C_Entry, T_list, Columns, Values):
    
    sql_set = bftn.mysql_set(con.config)
    select_data = bftn.get_selectitem(Frame_class, T_list)
    if select_data != False:
        query_value = select_data + "', '" + Values
        conditions = "class_name IS NOT NULL"
        sql_set.insert_query_str(Columns, query_value)
        bftn.clear(C_Entry)
        bftn.show_list_box_cond(C_List, "class_name", conditions)
        ########################
        # teacher = select_data 인 항목만 가져오도록 수정...
        ########################
    else:
        print("aa")
    
    
    
    
