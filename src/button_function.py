import pymysql


import config_set as con
import base_function as bftn


# db_conn_config = con.config

def add_T_listbox(Frame_class, T_List, T_Entry, Columns, Values):

    ## T_Entry, Values 중복...
    if Values != "":
        sql_set = bftn.mysql_set(con.config)
        sql_set.insert_query_str(Columns, Values)
        bftn.clear(T_Entry)
        bftn.show_list_box(T_List, "teacher")
    else:
        sub_wd = Frame_class.sub_wd()
        bftn.Input_Error(sub_wd, "내용을 입력해주세요.")
    
    
def add_C_listbox(Frame_class, C_List, C_Entry, T_list, Columns, Values):
    
    sql_set = bftn.mysql_set(con.config)
    select_data = bftn.get_selectitem(Frame_class, T_list)
    if select_data != False:
        bftn.clear(C_List)
        if Values != "":
            query_value = bftn.str_combine(select_data, Values)
            conditions = f"class_name IS NOT NULL AND teacher = '{select_data}'"
            sql_set.insert_query_str(Columns, query_value)
            bftn.clear(C_Entry)
            bftn.show_list_box_cond(C_List, "class_name", conditions)
        else:
            sub_wd = Frame_class.sub_wd()
            bftn.Input_Error(sub_wd, "내용을 입력해주세요.")
    else:
        sub_wd = Frame_class.sub_wd()
        bftn.Input_Error(sub_wd, "선생님 항목을 선택하십시오.")
    
    
    
    
