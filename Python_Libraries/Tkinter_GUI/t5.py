from tkinter import *
imag_root=Tk()

imag_root.geometry("100x100")
photo=PhotoImage(file="s.png")

var_label=Label(image=photo)
var_label.pack()

imag_root.mainloop()
