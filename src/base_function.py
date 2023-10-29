import tkinter as tk
from tkinter import ttk

def clear_entry(target):
    target.delete(0, tk.END) 
    

        
class window_set:
    def __init__(self, window):
        self.new_window = window
        self.button = ""
        self.label = ""
        self.entry = ""
        self.text = ""
        
        
    def set_title(self, title):
        self.new_window.title(title)
        
    def set_size(self, screen_size):
        self.new_window.geometry(screen_size)
              
    def set_fullscreen(self):
        self.new_window.bind("<F11>", lambda event: self.new_window.attributes("-fullscreen", not self.new_window.attributes("-fullscreen")))
        self.new_window.bind("<Escape>", lambda event: self.new_window.attributes("-fullscreen", False))
        
    def gen_button(self, bt_text, cm_ftn, b_x, b_y):
        self.button = tk.Button(self.new_window, text=bt_text, command=cm_ftn)
        self.button.place(x=b_x, y=b_y)
        
    def gen_button_bs(self, bt_text, cm_ftn, width, height, b_x, b_y):
        self.button = tk.Button(self.new_window, text=bt_text, width=width, height=height, command=cm_ftn)
        self.button.place(x=b_x, y=b_y)
        
    def gen_button_fs(self, bt_text, cm_ftn, b_x, b_y, font=1):
        self.button = tk.Button(self.new_window, text=bt_text, command=cm_ftn, font=font)
        self.button.place(x=b_x, y=b_y)
        
    def gen_Frame(self, width, height, bg):
        return tk.Frame(self.new_window, width=width, height=height, bg=bg)
    
    def gen_Frame_nobg(self, width, height):
        return tk.Frame(self.new_window, width=width, height=height)
        
    def gen_label(self, label_text):
        self.label = tk.Label(text=label_text)
        self.label.pack(pady=10)
        
    def gen_label_rely_fs(self, lb_text, l_x, l_rely, font=10):
        self.label = tk.Label(self.new_window, text=lb_text, font=font)
        self.label.place(x=l_x, rely=l_rely)
        
    def gen_notebook(self, width, height):
        return ttk.Notebook(self.new_window, width=width, height=height)
        
    def insert_image(self, image_path, i_x, i_y):
        photo = tk.PhotoImage(file=image_path)
        imgInsert = tk.Label(self.new_window, image=photo)
        imgInsert.place(x=i_x, y=i_y)
        
    def insert_label_entry(self, var, title, l_x, l_y, e_x, e_y, L_width=7, E_width=17):
        self.label = tk.Label(self.new_window, text=title, width=L_width, anchor="e")
        self.label.place(x=l_x, y=l_y)
        self.entry = tk.Entry(self.new_window, width=E_width, textvariable=var)
        self.entry.place(x=e_x, y=e_y)
        
    def insert_label_text(self, lb_text, l_x, l_y, e_x, e_y, L_width=7, T_width=15, height=1):
        self.label = tk.Label(self.new_window, text=lb_text, width=L_width)
        self.label.place(x=l_x, y=l_y)
        self.text = tk.Text(self.new_window, width=T_width, height=height)
        self.text.place(x=e_x, y=e_y)
        
    def pack(self, side, fill, expand):
        self.new_window.pack(side=side, fill=fill, expand=expand)
        
    # def wd(self):
    #     return self.new_window
        
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