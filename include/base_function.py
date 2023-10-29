import tkinter as tk


def clear_entry(target):
    target.delete(0, tk.END) 
    

        
class window_set:
    def __init__(self, window):
        self.new_window = window
        
        
    def set_title(self, title):
        self.new_window.title(title)
        
    def set_size(self, screen_size):
        self.new_window.geometry(screen_size)
              
    def set_fullscreen(self):
        self.new_window.bind("<F11>", lambda event: self.new_window.attributes("-fullscreen", not self.new_window.attributes("-fullscreen")))
        self.new_window.bind("<Escape>", lambda event: self.new_window.attributes("-fullscreen", False))
        
    def gen_button(self, bt_text, cm_ftn):
        self.button = tk.Button(self.new_window, text=bt_text, command=cm_ftn)
        self.button.pack()
        
    def gen_Frame(self, width, height, bg):
        return tk.Frame(self.new_window, width=width, height=height, bg=bg)
        
    def set_baselabel(self, label_text):
        self.label = tk.Label(text=label_text)
        self.label.pack(pady=10)
        
    def button_click(self):
        self.label.config(text="버튼이 클릭되었습니다!")
        
    def gen_label(self, text):
        self.label(text=text)
        
    def clear_wd(self):
        self.new_window.destroy()
        
        