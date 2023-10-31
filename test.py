import tkinter as tk

root = tk.Tk()
root.title("이미지 삽입 예제")

photo = tk.PhotoImage(file="picture\photo_min.png")
photo_subsample = photo.subsample(10, 10)
label = tk.Label(root, image=photo_subsample)
label.pack()

root.mainloop()