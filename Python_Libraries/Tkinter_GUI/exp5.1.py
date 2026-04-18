from tkinter import *

def getvals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")
    print(f"The value of password is {Dept.get()}")

root = Tk()
root.geometry("655x333")
frame2 = LabelFrame(root, text='Gender', padx=30, pady=10)
Regno = Label(root, text="Regno")
Name = Label(root, text="Name :")
Dept = Label(root, text="Dept")

Regno.grid(row=0)
Name.grid(row=1)
Dept.grid(row=2)

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()
Deptvalue = StringVar()

userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)
Deptentry = Entry(root,text="Hello", textvariable = Deptvalue)
Radiobutton(frame2, text='Male', variable=var, value=2,command=selection).pack(anchor=W)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)
Deptentry.grid(row=2, column=1)

Button(text="Submit", command=getvals).grid()

root.mainloop()