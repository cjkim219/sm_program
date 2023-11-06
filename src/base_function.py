import tkinter as tk
from tkinter import ttk
import pymysql

import config_set as con

def clear(target):
    target.delete(0, tk.END) 
    
        
class window_set:
    def __init__(self, window):
        self.new_window = window
        self.button = ""
        self.label = ""
        self.entry = ""
        self.text = ""
        self.listbox = ""
        
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
    
    def gen_list_box(self, pos, rely):
        self.listbox = tk.Listbox(self.new_window, width=13, height=13, selectmode="single")
        self.listbox.configure(font=10)
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
    def insert_label_text(self, lb_text, l_x, l_y, e_x, e_y, L_width=7, T_width=15, height=1):
        self.label = tk.Label(self.new_window, text=lb_text, width=L_width)
        self.label.place(x=l_x, y=l_y)
        self.text = tk.Text(self.new_window, width=T_width, height=height)
        self.text.place(x=e_x, y=e_y)
        
    # place는 해당 좌표에 상자가 만들어지는데 pack은 좌, 위, 상, 하 등의 정렬을 할 수 있음. 단점은 세부 컨트롤이 어려움.
    def pack(self, side, fill, expand):
        self.new_window.pack(side=side, fill=fill, expand=expand)
        
    def sub_wd(self):
        return tk.Toplevel(self.new_window)
        
    # 창을 종료시키는 메서드
    def clear_wd(self):
        self.new_window.destroy()
        
        
        
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
    
    
    
    
class mysql_set:
    def __init__(self, config):
        self.config = config
        self.strdata = []
        self.result = []
        
    ### mysql query functions
    def insert_query_value(self, columns, values):
        conn = pymysql.connect(**self.config)
        
        try:
            with conn.cursor() as cur:
                # sql = "INSERT INTO 테이블명 (열1, 열2, 열3) VALUES (%s, %s, %s)"
                sql = f"INSERT INTO main_table ({columns}) VALUES ({values})"
                print(sql)
                # sql = "INSERT INTO " + con.table_name + " " + "(" + columns + ")" +" VALUES " + "(" + values + ")"
                ######################
                ## sql string 편집
                ######################
                    
                cur.execute(sql)
                conn.commit()
                    
        except SyntaxError:
            print("syntax error")
            
        finally:
            conn.close()
            
            
    def insert_query_str(self, columns, values):
        conn = pymysql.connect(**self.config)
        
        try:
            with conn.cursor() as cur:
                sql = f"INSERT INTO main_table ({columns}) VALUES ('{values}')"
                cur.execute(sql)
                conn.commit()
                    
        except SyntaxError:
            print("syntax error")
            
        finally:
            conn.close()
            

    def select_query(self, columns, conditions):
        conn = pymysql.connect(**self.config)
        
        try:
            with conn.cursor() as cur:
                # sql = "SELECT 열1, 열2 FROM 테이블명 WHERE 조건"
                sql = f"SELECT {columns} FROM {con.table_name} WHERE {conditions}"
                ######################
                ## sql string 편집
                ######################
                
                cur.execute(sql)
                result = cur.fetchall()    # result = cur.fetchone()
                
                # for row in result:
                #     print(row)
                    
        except SyntaxError:
            print("syntax error")
            
        finally:
            conn.close()
            
        return result
    
    
    def select_query_distinct_cond(self, columns, conditions):
        conn = pymysql.connect(**self.config)
        
        try:
            with conn.cursor() as cur:
                sql = f"SELECT DISTINCT {columns} FROM {con.table_name} WHERE {conditions}"
                print(sql)
                cur.execute(sql)
                result = cur.fetchall()
                    
        except SyntaxError:
            print("syntax error")
            
        finally:
            conn.close()
            
        return result
    
    
    def select_query_distinct(self, columns):
        conn = pymysql.connect(**self.config)
        
        try:
            with conn.cursor() as cur:
                sql = f"SELECT DISTINCT {columns} FROM {con.table_name}"
                cur.execute(sql)
                result = cur.fetchall()
                    
        except SyntaxError:
            print("syntax error")
            
        finally:
            conn.close()
            
        return result
    
    
    
def show_list_box_cond(Listbox, columns, conditions):
    
    sql_set = mysql_set(con.config)
    res = sql_set.select_query_distinct_cond(columns, conditions)
    clear(Listbox)
    for row in res:
        Listbox.insert(tk.END, row)
        
        
def show_list_box(Listbox, columns):
    
    sql_set = mysql_set(con.config)
    res = sql_set.select_query_distinct(columns)
    clear(Listbox)
    for row in res:
        Listbox.insert(tk.END, row)
        


def get_selectitem(Frame_class, T_list):
        
    index = T_list.curselection()
    
    if index:
        item = str(T_list.get(index))
        return item[2:len(item)-3]
        
    else:
        sub_wd = Frame_class.sub_wd()
        sub_wd.title("오류")
        label = tk.Label(sub_wd, text="선생님 항목을 선택해주세요.", anchor="center")
        label.place(x=10, y=10)
        btn = tk.Button(sub_wd, text="확인", command=sub_wd.destroy)
        btn.place(x=10, y=30)
        return False
        
    