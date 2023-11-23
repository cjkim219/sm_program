# from tkinter import *
# from tkinter import ttk
# # import mysql.connector
# import pymysql



# # mariaDB 접속 정보
# config = {
#     'user': 'root',
#     'password': '123!',
#     'host': '127.0.0.1',
#     'database': 'info',
# }


# con, cur = None, None
# sql = ""

# conn = pymysql.connect(**config)
# cur = conn.cursor()

# # sql = "INSERT INTO 테이블명 (열1, 열2, 열3) VALUES (%s, %s, %s)"
# # INSERT INTO `info`.`main_table` (`선생님`) VALUES ('부원장');

# # sql = "INSERT INTO main_table (teacher) VALUES('테스트')"
# columns = "teacher"
# values = "부원장"
# sql = f"INSERT INTO main_table ({columns}) VALUES ('{values}')"
# print(sql)
# cur.execute(sql)


# conn.commit()
# conn.close()

# def clear_entry(target):
#     target.delete(0, END)
    

# def insertData():
#     con, cur = None, None
#     data1 = "" 
#     data2 = ""
#     data3 = ""
#     data4 = ""
#     sql = ""
    
#     conn = pymysql.connect(**config)
#     cur = conn.cursor()
    
#     data1 = edt1.get()
#     data2 = edt2.get()
#     data3 = edt3.get()
#     data4 = edt4.get()
    
#     sql = "INSERT INTO main_table VALUES('" + data1 + "', '" + data2 + "', '" + data3 + "', '" + data4 + "')"
    
#     cur.execute(sql)

#     clear_entry(edt1)
#     clear_entry(edt2)
#     clear_entry(edt3)
#     clear_entry(edt4)
    
#     conn.commit()
#     conn.close()
    
        
# def selectData():
#     strData1, strData2, strData3, strData4 = [], [], [], []
    
#     conn = pymysql.connect(**config)
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM main_table")
    
#     strData1.append("이름")
#     strData2.append("나이")
#     strData3.append("날짜")
#     strData4.append("내용")
#     strData1.append("-------")
#     strData2.append("-------")
#     strData3.append("-------")
#     strData4.append("-------")
    
#     while(True):
#         row = cur.fetchone()
#         if row == None:
#             break
#         strData1.append(row[0])
#         strData2.append(row[1])
#         strData3.append(row[2])
#         strData4.append(row[3])
        
#     listData1.delete(0, listData1.size() - 1)
#     listData2.delete(0, listData2.size() - 1)
#     listData3.delete(0, listData3.size() - 1)
#     listData4.delete(0, listData4.size() - 1)
    
#     for item1, item2, item3, item4 in zip(strData1, strData2, strData3, strData4):
#         listData1.insert(END, item1)
#         listData2.insert(END, item2)
#         listData3.insert(END, item3)
#         listData4.insert(END, item4)
    
#     conn.close()
    
    



# # edtFrame = Frame(main_wd)
# # edtFrame.pack()
# # listFrame = Frame(main_wd)
# # listFrame.pack(side = BOTTOM, fill=BOTH, expand=1)

# edt1 = Entry(edtFrame, width=10)

# edt1.dele

# edt1.pack(side=LEFT, padx=10, pady=10)
# edt2 = Entry(edtFrame, width=10)
# edt2.pack(side=LEFT, padx=10, pady=10)
# edt3 = Entry(edtFrame, width=10)
# edt3.pack(side=LEFT, padx=10, pady=10)
# edt4 = Entry(edtFrame, width=10)
# edt4.pack(side=LEFT, padx=10, pady=10)

# # listData1 = Listbox(listFrame)
# # listData1.pack(side=LEFT, fill=BOTH, expand=1)
# # listData2 = Listbox(listFrame)
# # listData2.pack(side=LEFT, fill=BOTH, expand=1)
# # listData3 = Listbox(listFrame)
# # listData3.pack(side=LEFT, fill=BOTH, expand=1)
# # listData4 = Listbox(listFrame)
# # listData4.pack(side=LEFT, fill=BOTH, expand=1)
    
    

# # # py 파일 추가해서 3줄만 다른곳으로 옮겨보기.
# # # window.attributes("-fullscreen", True)


# # login_wd.mainloop()



# # # py 파일 추가해서 3줄만 다른곳으로 옮겨보기.
# # # window.attributes("-fullscreen", True)
# # login_wd.bind("<F11>", lambda event: login_wd.attributes("-fullscreen", not login_wd.attributes("-fullscreen")))
# # login_wd.bind("<Escape>", lambda event: login_wd.attributes("-fullscreen", False))





# sample_list = ['age', 'gender']

# print(sample_list)

# sample_str = str()

# for val in sample_list:
#     print(val)
#     sample_str += (val + ", ")
    
    
# print(sample_str[0:len(sample_str)-2])

import tkinter as tk
from tkinter import ttk

def update_combobox():
    # 업데이트할 목록
    new_items = ["항목1", "항목2", "항목3"]

    # 콤보박스의 목록 업데이트
    combo['values'] = new_items

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("콤보박스 리스트 업데이트 예제")

# 콤보박스 생성
combo = ttk.Combobox(window, values=["기존항목1", "기존항목2", "기존항목3"])
combo.pack(padx=10, pady=10)

# 업데이트 버튼 생성
update_button = tk.Button(window, text="리스트 업데이트", command=update_combobox)
update_button.pack(pady=10)

# 윈도우 실행
window.mainloop()