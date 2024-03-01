import tkinter as tk
from tkinter import ttk

from datetime import datetime

import pymysql


import config_set as con


class window_set:
    def __init__(self, window):
        self.new_window = window
        self.button = ""
        self.label = ""
        self.entry = ""
        self.text = ""
        self.listbox = ""
        self.combobox = ""
        
    def set_title(self, title):
        self.new_window.title(title)
        
    def set_size(self, screen_size):
        self.new_window.geometry(screen_size)
              
    def set_fullscreen(self):
        self.new_window.bind("<F11>", lambda event: self.new_window.attributes("-fullscreen", not self.new_window.attributes("-fullscreen")))
        self.new_window.bind("<Escape>", lambda event: self.new_window.attributes("-fullscreen", False))
        
    # 버튼 생성 메서드 (버튼 텍스트, 버튼 클릭시 실행할 함수, 버튼 x좌표, 버튼 y좌표)
    def gen_button(self, bt_text, cm_ftn, b_x, b_y):
        self.button = tk.Button(self.new_window, text=bt_text, command=cm_ftn)
        self.button.place(x=b_x, y=b_y)
        return self.button
    
    # 버튼 생성 메서드 + 버튼 크기 조절 (width, height)  
    def gen_button_bs(self, bt_text, cm_ftn, width, height, b_x, b_y):
        self.button = tk.Button(self.new_window, text=bt_text, width=width, height=height, command=cm_ftn)
        self.button.place(x=b_x, y=b_y)
        
    # 버튼 생성 메서드 + 버튼 폰트 크기 조절 // font값에 따라 폰트 크기가 안변하던데... 확인 필요
    def gen_button_fs(self, bt_text, cm_ftn, b_x, b_y, font=1):
        self.button = tk.Button(self.new_window, text=bt_text, command=cm_ftn, font=font)
        self.button.place(x=b_x, y=b_y)
    
    # 프래임 생성 메서드 - main window 내부를 구획으로 나누는 sub window 느낌 (bg는 배경 색상 선택)
    def gen_Frame(self, width, height, bg):
        return tk.Frame(self.new_window, width=width, height=height, bg=bg)
    
    def gen_Frame_nobg(self, width, height):
        return tk.Frame(self.new_window, width=width, height=height)
        
    # 라벨 생성 메서드
    def gen_label(self, label_text, l_x, l_y):
        self.label = tk.Label(self.new_window, text=label_text)
        self.label.place(x=l_x, y=l_y)
                
        
    def gen_entry(self, var, e_x, e_y, E_width):
        self.entry = tk.Entry(self.new_window, width=E_width, textvariable=var)
        self.entry.place(x=e_x, y=e_y)
        return self.entry
        
    
    def gen_textbox(self, t_x, t_y, T_width, height):
        self.text = tk.Text(self.new_window, width=T_width, height=height)
        self.text.place(x=t_x, y=t_y)
        
        
    def label_ntxt(self, new_text):
        self.label.config(text=new_text)
        
    # 라벨 생성 메서드 + 라벨 폰트 크기 조절 + 위치를 좌표 대신 배율로 조정
    # (버튼과 마찬가지로.. 폰트 크기가 변하지 않음.. 조금 커지는정도)
    # rely = 0.1 로 설정하면 프래임을 0~1 중 1/10에 위치하는 곳에 배치시킴.
    # 사용자의 화면 배율이 모두 제각각일 것이라 좌표를 이용해 배치하는것보다 나중엔 rel을 써야할듯...
    def gen_label_rely_fs(self, lb_text, l_x, l_rely, font=10):
        self.label = tk.Label(self.new_window, text=lb_text, font=font)
        self.label.place(x=l_x, rely=l_rely)
        
    def gen_label_rely(self, lb_text, l_x, l_rely):
        self.label = tk.Label(self.new_window, text=lb_text)
        self.label.place(x=l_x, rely=l_rely)
        
    # 탭을 만들 수 있는 몸통(?)프래임을 만들어주는 메서드
    # ex) 기본정보 + 수업정보 + 상담내용 + 성적결과 네 개의 탭이 하나의 노트북에 담김
    def gen_notebook(self, width, height):
        return ttk.Notebook(self.new_window, width=width, height=height)
    
    def gen_combobox(self, options, C_width, c_x, c_y):
        self.combobox = ttk.Combobox(self.new_window, values=options, width=C_width)
        self.combobox.place(x=c_x, y=c_y)
        return self.combobox
    
    def gen_listbox_fs(self, pos, rely):
        self.listbox = tk.Listbox(self.new_window, width=13, height=13, selectmode="browse", activestyle="none")
        self.listbox.configure(font=10)
        self.listbox.place(x=pos, rely=rely)
        return self.listbox
    
    def gen_listbox_bs(self, pos, rely, Lb_width, Lb_height):
        self.listbox = tk.Listbox(self.new_window, width=Lb_width, height=Lb_height, selectmode="browse", activestyle="none")
        self.listbox.place(x=pos, rely=rely)
        return self.listbox
        
    # 이미지 삽입 메서드, subsample이라는 메서드로 그림 크기를 해당 배율만큼 줄여줌. (15, 15) -> 가로, 세로 15배 축소
    def insert_image(self, image_path, i_x, i_y):
        photo = tk.PhotoImage(file=image_path)
        photo_sub = photo.subsample(10, 10)
        imgInsert = tk.Label(self.new_window, image=photo_sub)
        imgInsert.image = photo_sub
        imgInsert.place(x=i_x, y=i_y)
        
    # 라벨 + 엔트리 삽입 메서드, 엔트리는 텍스트를 입력할 수 있는 공간이며 입력받은 값을 변수로 활용 가능.
    # l_x, l_y 는 라벨의 x, y 좌표이며 e_x, e_y는 엔트리의 x, y좌표, L_width는 라벨의 너비, E_width는 엔트리의 너비
    # 엔트리는 한줄밖에 입력할 수 없어서 주소, 특이사항 같은 넓은 칸이 필요한 곳은 엔트리 대신 text로 대체함.
    # 문제는... text에 입력된 값을 변수로 받아서 활용하기 불편할 것임... 가능할 것 같은데 확인 필요.
    def insert_label_entry(self, var, title, l_x, l_y, e_x, e_y, L_width=7, E_width=17):
        self.label = tk.Label(self.new_window, text=title, width=L_width, anchor="e")
        self.label.place(x=l_x, y=l_y)
        self.entry = tk.Entry(self.new_window, width=E_width, textvariable=var)
        self.entry.place(x=e_x, y=e_y)
        
    def insert_label_entry_show(self, var, title, show_str, l_x, l_y, e_x, e_y, L_width=7, E_width=17):
        self.label = tk.Label(self.new_window, text=title, width=L_width, anchor="e")
        self.label.place(x=l_x, y=l_y)
        self.entry = tk.Entry(self.new_window, show=show_str, width=E_width, textvariable=var)
        self.entry.place(x=e_x, y=e_y)
        
    # 라벨 + 텍스트 삽입 메서드, height는 텍스트 라인 갯수를 의미함.
    def insert_label_text(self, lb_text, l_x, l_y, t_x, t_y, L_width=7, T_width=15, height=1):
        self.label = tk.Label(self.new_window, text=lb_text, width=L_width)
        self.label.place(x=l_x, y=l_y)
        self.text = tk.Text(self.new_window, width=T_width, height=height)
        self.text.place(x=t_x, y=t_y)
        return self.text
        
    # place는 해당 좌표에 상자가 만들어지는데 pack은 좌, 위, 상, 하 등의 정렬을 할 수 있음. 단점은 세부 컨트롤이 어려움.
    def pack(self, side, fill, expand):
        self.new_window.pack(side=side, fill=fill, expand=expand)
        
    def sub_wd(self):
        return tk.Toplevel(self.new_window)
        
    # 창을 종료시키는 메서드
    def clear_wd(self):
        self.new_window.destroy()
        
        
        

class mysql_set:
    def __init__(self, config):
        self.config = config
        self.strdata = []
        self.result = []
        
    ### mysql query functions
    def insert_query_value(self, columns, values, table = con.table_name):
        conn = pymysql.connect(**self.config)
        
        try:
            with conn.cursor() as cur:
                sql = f"INSERT INTO {table} ({columns}) VALUES ({values})"             
                cur.execute(sql)
                conn.commit()
                    
        except SyntaxError:
            print("syntax error")
            
        finally:
            conn.close()
            
            
    def insert_query_str(self, columns, values, table = con.table_name):
        conn = pymysql.connect(**self.config)
        
        try:
            with conn.cursor() as cur:
                sql = f"INSERT INTO {table} ({columns}) VALUES ('{values}')"
                cur.execute(sql)
                conn.commit()
                    
        except SyntaxError:
            print("syntax error")
            
        finally:
            conn.close()
            

    def select_query(self, columns, conditions, table = con.table_name):
        conn = pymysql.connect(**self.config)
        
        try:
            with conn.cursor() as cur:
                sql = f"SELECT {columns} FROM {table} WHERE {conditions}"
                cur.execute(sql)
                result = cur.fetchall()    
                    
        except SyntaxError:
            print("syntax error")
            
        finally:
            conn.close()
            
        return result
    
    
    def select_query_distinct(self, columns, table = con.table_name):
        conn = pymysql.connect(**self.config)
        
        try:
            with conn.cursor() as cur:
                sql = f"SELECT DISTINCT {columns} FROM {table}"
                cur.execute(sql)
                result = cur.fetchall()
                    
        except SyntaxError:
            print("syntax error")
            
        finally:
            conn.close()
            
        return result
    
    
    def select_query_distinct_cond(self, columns, conditions, table = con.table_name):
        conn = pymysql.connect(**self.config)
        
        try:
            with conn.cursor() as cur:
                sql = f"SELECT DISTINCT {columns} FROM {table} WHERE {conditions}"
                cur.execute(sql)
                result = cur.fetchall()
                    
        except SyntaxError:
            print("syntax error")
            
        finally:
            conn.close()
            
        return result
    
    
    def select_order_query(self, columns, conditions, order_column, table = con.table_name):
        conn = pymysql.connect(**self.config)
        
        try:
            with conn.cursor() as cur:
                sql = f"SELECT {columns} FROM {table} WHERE {conditions} ORDER BY {order_column}"
                cur.execute(sql)
                result = cur.fetchall()    
                    
        except SyntaxError:
            print("syntax error")
            
        finally:
            conn.close()
            
        return result
    
    
    def select_order_query_distinct(self, columns, order_column, table = con.table_name):
        conn = pymysql.connect(**self.config)
        
        try:
            with conn.cursor() as cur:
                sql = f"SELECT DISTINCT {columns} FROM {table} ORDER BY {order_column}"
                cur.execute(sql)
                result = cur.fetchall()
                    
        except SyntaxError:
            print("syntax error")
            
        finally:
            conn.close()
            
        return result
    
    
    def select_order_query_distinct_cond(self, columns, conditions, order_column, table = con.table_name):
        conn = pymysql.connect(**self.config)
        
        try:
            with conn.cursor() as cur:
                sql = f"SELECT DISTINCT {columns} FROM {table} WHERE {conditions} ORDER BY {order_column}"
                cur.execute(sql)
                result = cur.fetchall()
                    
        except SyntaxError:
            print("syntax error")
            
        finally:
            conn.close()
            
        return result
    
    
    def delete_query_cond(self, conditions, table = con.table_name):
        conn = pymysql.connect(**self.config)
    
        try:
            with conn.cursor() as cur:
                sql = f"DELETE FROM {table} WHERE {conditions}"
                cur.execute(sql)
                conn.commit()
                    
        except SyntaxError:
            print("syntax error")
            
        finally:
            conn.close()
            
            
    def update_query_value(self, update_data, conditions, table = con.table_name):
        conn = pymysql.connect(**self.config)
    
        try:
            with conn.cursor() as cur:
                sql = f"UPDATE {table} SET {update_data} WHERE {conditions}"
                cur.execute(sql)
                conn.commit()
                    
        except SyntaxError:
            print("syntax error")
            
        finally:
            conn.close()
            
            


class student_info:
    def __init__(self):
        self.age_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.school_var = tk.StringVar()
        self.grade_var = tk.StringVar()
        self.birth_var = tk.StringVar()
        self.st_HP_var = tk.StringVar()
        self.pa_HP_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address = tk.Text()
        self.etc = tk.Text()
        
        self.course_var = tk.StringVar()
        self.class_day_var = tk.StringVar()
        self.day1_var = tk.StringVar()
        self.day2_var = tk.StringVar()
        self.day3_var = tk.StringVar()
        self.day1_start_var = tk.StringVar()
        self.day1_end_var = tk.StringVar()
        self.day2_start_var = tk.StringVar()
        self.day2_end_var = tk.StringVar()
        self.day3_start_var = tk.StringVar()
        self.day3_end_var = tk.StringVar()
        
        self.main_book_var = tk.StringVar()
        self.main_start_date_var = tk.StringVar()
        self.main_end_date_var = tk.StringVar()
        self.sub_book_var = tk.StringVar()
        self.sub_start_date_var = tk.StringVar()
        self.sub_end_date_var = tk.StringVar()
        self.text1 = tk.Text()
        self.text2_var = tk.StringVar()
        
    
    def clear(self):
        self.age_var.set("")
        self.gender_var.set("")
        self.school_var.set("")
        self.grade_var.set("")
        self.birth_var.set("")
        self.st_HP_var.set("")
        self.pa_HP_var.set("")
        self.email_var.set("")
        self.address.delete("1.0", tk.END)
        self.etc.delete("1.0", tk.END)
        
        self.course_var.set("")
        self.class_day_var.set("")
        self.day1_var.set("")
        self.day2_var.set("")
        self.day3_var.set("")
        self.day1_start_var.set("")
        self.day1_end_var.set("")
        self.day2_start_var.set("")
        self.day2_end_var.set("")
        self.day3_start_var.set("")
        self.day3_end_var.set("")
        
        self.main_book_var.set("")
        self.main_start_date_var.set("")
        self.main_end_date_var.set("")
        self.sub_book_var.set("")
        self.sub_start_date_var.set("")
        self.sub_end_date_var.set("")
        self.text1.delete("1.0", tk.END)
        self.text2_var.set("")


        
class consult_content:
    def __init__(self):
        self.date_var = tk.StringVar()
        self.subject_var = tk.StringVar()
        self.content = tk.Text()
        
    def clear(self):
        self.date_var.set("")
        self.subject_var.set("")
        self.content.delete("1.0", tk.END)
        
    def get(self):
        return self.subject_var.get(), self.date_var.get(), self.content.get("1.0", tk.END)
        
        
class exam_content:
    def __init__(self):
        self.date_var = tk.StringVar()
        self.exam_type_var = tk.StringVar()
        self.exam_range_var = tk.StringVar()
        self.score_var = tk.StringVar()
        
    def clear(self):
        self.date_var.set("")
        self.exam_type_var.set("")
        self.exam_range_var.set("")
        self.score_var.set("")
        
        
        
            
def clear(target):
    target.delete(0, tk.END)
    
    
    
def insert_label_entry(Frame, var, title, l_x, l_y, e_x, e_y, L_width=7, E_width=17):
    label = tk.Label(Frame, text=title, width=L_width, anchor="e")
    label.place(x=l_x, y=l_y)
    entry = tk.Entry(Frame, width=E_width, textvariable=var)
    entry.place(x=e_x, y=e_y)
    
    
    
def insert_label_text(Frame, lb_text, l_x, l_y, e_x, e_y, L_width=7, T_width=15, height=1):
    label = tk.Label(Frame, text=lb_text, width=L_width)
    label.place(x=l_x, y=l_y)
    text = tk.Text(Frame, width=T_width, height=height)
    text.place(x=e_x, y=e_y)
    
    
    
def gen_button_fs(Frame, bt_text, cm_ftn, b_x, b_y, font=1):
    button = tk.Button(Frame, text=bt_text, command=cm_ftn, font=font)
    button.place(x=b_x, y=b_y)
    
    
    
def gen_label_rely(Frame, lb_text, l_x, l_rely):
    label = tk.Label(Frame, text=lb_text)
    label.place(x=l_x, rely=l_rely)
    
    
        
def show_info_cond(info_class, conditions):
    
    sql_set = mysql_set(con.config)
    res = sql_set.select_query("*", conditions)
    
    info_class.clear()
    for i in range(3, con.db_info_length):
        if res[0][i] != None:
            show_value(i, info_class, res[0][i])
            
            
            
def show_consult_info_cond(info_class, conditions):
    
    sql_set = mysql_set(con.config)
    res = sql_set.select_query("*", conditions, con.consult_table_name)
    
    info_class.clear()
    for i in range(2, con.db_consult_info_length):
        if res[0][i] != None:
            show_consult_value(i, info_class, res[0][i])



def show_consult_value(int, consult_content, value):
    if int == 2:
        consult_content.date_var.set(value)
    elif int == 3:
        consult_content.subject_var.set(value)
    elif int == 4:
        consult_content.content.insert(tk.END, value)
        
        
            
def show_value(int, student_info, value):
    if int == 3:
        student_info.age_var.set(value)
    elif int == 4:
        student_info.gender_var.set(value)
    elif int == 5:
        student_info.school_var.set(value)
    elif int == 6:
        student_info.grade_var.set(value)
    elif int == 7:
        student_info.birth_var.set(value)
    elif int == 8:
        student_info.st_HP_var.set(value)
    elif int == 9:
        student_info.pa_HP_var.set(value)
    elif int == 10:
        student_info.email_var.set(value)
    elif int == 11:
        student_info.address.insert(tk.END, value)
    elif int == 12:
        student_info.etc.insert(tk.END, value)
    elif int == 13:
        student_info.course_var.set(value)
    elif int == 14:
        student_info.class_day_var.set(value)
    elif int == 15:
        student_info.day1_var.set(value)
    elif int == 16:
        student_info.day2_var.set(value)
    elif int == 17:
        student_info.day3_var.set(value)
    elif int == 18:
        student_info.day1_start_var.set(value)
    elif int == 19:
        student_info.day1_end_var.set(value)
    elif int == 20:
        student_info.day2_start_var.set(value)
    elif int == 21:
        student_info.day2_end_var.set(value)
    elif int == 22:
        student_info.day3_start_var.set(value)
    elif int == 23:
        student_info.day3_end_var.set(value)
    elif int == 24:
        student_info.main_book_var.set(value)
    elif int == 25:
        student_info.main_start_date_var.set(value)
    elif int == 26:
        student_info.main_end_date_var.set(value)
    elif int == 27:
        student_info.sub_book_var.set(value)
    elif int == 28:
        student_info.sub_start_date_var.set(value)
    elif int == 29:
        student_info.sub_end_date_var.set(value)
    elif int == 30:
        student_info.text1.insert(tk.END, value)
    elif int == 31:
        student_info.text2_var.set(value)
            
        
        
def show_list_box(Listbox, columns, order_column):
    
    sql_set = mysql_set(con.config)
    res = sql_set.select_order_query_distinct(columns, order_column)
    clear(Listbox)
    for row in res:
        Listbox.insert(tk.END, row)
        
        
        
def show_list_box_cond(Listbox, columns, conditions, order_column, table = con.table_name):
    
    sql_set = mysql_set(con.config)
    res = sql_set.select_order_query_distinct_cond(columns, conditions, order_column, table)
    clear(Listbox)
    for row in res:
        Listbox.insert(tk.END, row)
        
        # select_order_query(self, columns, conditions, order_column, table = con.table_name):

def show_exam_list_box(Date_List, Type_List, Range_List, Score_List, conditions, order_column):
    
    sql_set = mysql_set(con.config)
    res = sql_set.select_order_query("*", conditions, order_column, con.exam_table_name)
    clear(Date_List)
    clear(Type_List)
    clear(Range_List)
    clear(Score_List)
    for row in res:
        Date_List.insert(tk.END, row[2])
        Type_List.insert(tk.END, row[3])
        Range_List.insert(tk.END, row[4])
        Score_List.insert(tk.END, row[5])


def get_selectitem(Frame_class, T_list, errorText):
        
    index = T_list.curselection()
    
    if index:
        return T_list.get(index)[0]
        
    else:
        sub_wd = Frame_class.sub_wd()
        Error_Box(sub_wd, errorText)
        return False
        
        

def str_combine(str_1, str_2):
    return str(str_1) + "', '" + str(str_2)



def Error_Box(sub_wd, text):
    sub_wd.title("오류")
    sub_wd.geometry(con.war_box_size)
    label = tk.Label(sub_wd, text=text, anchor="center")
    label.place(x=10, y=10)
    btn = tk.Button(sub_wd, text="확인", command=sub_wd.destroy)
    btn.place(x=10, y=30)
    
    
def authority_check(query_result, check_data):
    authority = False
    for val in query_result:
        if val[0] == check_data:
            authority = True
            break
    return authority


def authority_check_2(query_result, check_data):
    authority = False
    for val in query_result:
        if f"{val[1]}" == f"{check_data}":
            authority = True
            break
    return authority


def authority_check_tuple(query_result, check_data_1, check_data_2):
    authority = False

    for val in query_result:
        if f"{val[0]}" == f"{check_data_1}" and f"{val[1]}" == f"{check_data_2}":
            authority = True
            break
    return authority


def authority_check_val(query_result, check_data):
    authority = False
    for val in query_result:
        if val == check_data:
            authority = True
            break
    return authority


def add_col_val_list(list, col_num, val):
    
    if val == "":
        return 0
    elif val == "\n":
        return 0
    else:
        list.append(f"{con.column[col_num]} = '{val}'")
        
        
def add_col_val_list_consult(list, col_num, val):
    
    if val == "":
        return 0
    elif val == "\n":
        return 0
    else:
        list.append(f"{con.consult_column[col_num]} = '{val}'")
        
        
def get_text(tk_text):
    return tk_text.get("1.0", tk.END)
    
    
def list_to_str(list):
    
    string = str()
    
    for val in list:
        string += (val + ", ")
        
    return string[0:len(string)-2]


def list_to_val(list):
    
    string = str(list)
    
    return string[1:len(string)-1]



def add_table_query(start):
    conn = pymysql.connect(**con.config)
    
    try:
        with conn.cursor() as cur:
            for i in range(start, con.db_info_length):
                sql = f"ALTER TABLE {con.table_name} ADD COLUMN {con.column[i]} {con.column_type[i]}"
                cur.execute(sql)
            conn.commit()
                
    except SyntaxError:
        print("syntax error")
        
    finally:
        conn.close()
        
        
def combobox_list_update(cond, combobox, cond_column_1, cond_column_2, order_column):
    
    sql_set = mysql_set(con.config)
    
    update_list = []
    conditions = f"{cond_column_1} = '{cond}'"
    
    res = sql_set.select_order_query(f"{cond_column_2}", conditions, f"{order_column}", con.consult_table_name)

    for val in res:
        update_list.append(val[0].strftime("%Y-%m-%d"))

    combobox['values'] = update_list
    
    
    
# def get_option_date(cond, cond_column_1, cond_column_2):
    
#     sql_set = mysql_set(con.config)
    
#     option = []
#     conditions = f"{cond_column_1} = '{cond}'"
    
#     res = sql_set.select_query(f"{cond_column_2}", conditions, con.consult_table_name)

#     for val in res:
#         order_date = val[0]
#         formatted_date = order_date.strftime("%Y-%m-%d")
#         option.append(str(formatted_date))

#     return option
        
def today():
    now = datetime.now()

    year = now.year
    month = now.month
    day = now.day
    
    return f"{year}-{month}-{day}"



def set_today(entry):
    entry.set(today())