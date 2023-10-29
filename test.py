import tkinter as tk

root = tk.Tk()
root.title("이미지 삽입 예제")

photo = tk.PhotoImage(file="picture\photo.png")

label = tk.Label(root, image=photo)
label.pack()

root.mainloop()