import os

main_screen_title = "하이어 수학학원"
main_screen_size = "1080x720"

login_screen_title = "학생관리 프로그램"
login_screen_size = "296x240"

war_box_size = "200x80"


script_dir = os.path.dirname(os.path.abspath(__file__))
logo_directory = os.path.join(script_dir, r"..\..\..\images\higher_math_logo.png")
mid_frame_image = os.path.join(script_dir, r"..\..\..\images\mid_frame_image.png")


# logo_directory = r"..\images\higher_math_logo.png"
# mid_frame_image = r"..\images\mid_frame_image.png"


# host_ip = '127.0.0.1'
host_ip = '192.168.45.42'
port = 3306
db_name = 'info'

config = {'user': '',
          'password': '',
          'host': host_ip,
          'port': port,
          'database': db_name}


table_name = "main_table"

column = ["teacher", "class_name", "st_name", "age", "gender", "school", "grade", 
          "birth", "st_HP", "pa_HP", "email", "address", "etc", "course", "class_day",
          "day1", "day2", "day3", "day1_start", "day1_end", "day2_start", "day2_end",
          "day3_start", "day3_end", "main_book", "main_start", "main_end",
          "sub_book", "sub_start", "sub_end", "text1", "text"]

column_type = ["VARCHAR(50)", "VARCHAR(50)", "VARCHAR(50)", "CHAR(5)", "CHAR(5)", "VARCHAR(50)", "CHAR(5)", 
               "VARCHAR(50)", "VARCHAR(50)", "VARCHAR(50)", "VARCHAR(50)", "TEXT", "TEXT", "VARCHAR(50)",
               "CHAR(20)", "CHAR(5)", "CHAR(5)", "CHAR(5)", "CHAR(20)", "CHAR(20)", "CHAR(20)", "CHAR(20)",
               "CHAR(20)", "CHAR(20)", "VARCHAR(50)", "DATE", "DATE", "VARCHAR(50)", "DATE",
               "DATE", "TEXT", "VARCHAR(50)"]


consult_table_name = "consult"

consult_column = ["teacher", "st_name", "date", "subject", "content"]

consult_column_type = ["VARCHAR(50)", "VARCHAR(50)", "DATE", "VARCHAR(50)", "TEXT"]



exam_table_name = "exam_result"

exam_column = ["teacher", "st_name", "date", "exam_type", "exam_range", "score", "number"]

exam_column_type = ["VARCHAR(50)", "VARCHAR(50)", "DATE", "VARCHAR(50)", "VARCHAR(50)", "TINYINT", "SMALLINT"]



textbook_table_name = "textbook"

textbook_column = ["st_name", "main_book", "main_start", "main_end", "sub_book", "sub_start", "sub_end", "text"]

textbook_column_type = ["VARCHAR(50)", "VARCHAR(50)", "DATE", "DATE", "VARCHAR(50)", "DATE", "DATE", "VARCHAR(50)"]



class_time = ["17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00",
              "20:30", "21:00", "21:30", "22:00"]


db_info_length = len(column)
db_consult_info_length = len(consult_column)
db_exam_info_length = len(exam_column)

### global variable ###
selected_class_name = False
selected_st_name = False
selected_consult_date = ""