from ast import Num
from tkinter import *

root = Tk()
root.title("Calculator")

# making input field to take input form user
e = Entry(root, width=35, borderwidth=3)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def button_clear():
    e.delete(0, END)

def button_add():
    first_num = e.get()
    e.delete(0, END)
    global f_num
    f_num = int(first_num)
    global opr
    opr = "add"

def button_equal():
    second_num = int(e.get())
    e.delete(0, END)

    if opr=="add":
        e.insert(0, f_num + second_num)
    if opr=="mul":
        e.insert(0, f_num * second_num)
    if opr=="sub":
        e.insert(0, f_num - second_num)
    if opr=="div":
        e.insert(0, f_num / second_num)


def button_mul():
    first_num = e.get()
    e.delete(0, END)
    global f_num
    f_num = int(first_num)
    global opr
    opr = "mul"

def button_sub():
    first_num = e.get()
    e.delete(0, END)
    global f_num
    f_num = int(first_num)
    global opr
    opr = "sub"

def button_div():
    first_num = e.get()
    e.delete(0, END)
    global f_num
    f_num = int(first_num)
    global opr
    opr = "div"
    


button_7 = Button(root, text="7", padx=15, pady=10, command=lambda: button_click(7)).grid(row=1, column=0)
button_8 = Button(root, text="8", padx=15, pady=10, command=lambda: button_click(8)).grid(row=1, column=1)
button_9 = Button(root, text="9", padx=15, pady=10, command=lambda: button_click(9)).grid(row=1, column=2)

button_4 = Button(root, text="4", padx=15, pady=10, command=lambda: button_click(4)).grid(row=2, column=0)
button_5 = Button(root, text="5", padx=15, pady=10, command=lambda: button_click(5)).grid(row=2, column=1)
button_6 = Button(root, text="6", padx=15, pady=10, command=lambda: button_click(6)).grid(row=2, column=2)

button_1 = Button(root, text="1", padx=15, pady=10, command=lambda: button_click(1)).grid(row=3, column=0)
button_2 = Button(root, text="2", padx=15, pady=10, command=lambda: button_click(2)).grid(row=3, column=1)
button_3 = Button(root, text="3", padx=15, pady=10, command=lambda: button_click(3)).grid(row=3, column=2)

button_0 = Button(root, text="0", padx=15, pady=10, command=lambda: button_click(0)).grid(row=4, column=0)
button_clear = Button(root, text="Clear", padx=44, pady=10, command=button_clear).grid(row=4, column=1, columnspan=2)

button_add = Button(root, text="+", padx=14, pady=10, command=button_add).grid(row=5, column=0)
button_equal = Button(root, text="=", padx=54, pady=10, command=button_equal).grid(row=5, column=1, columnspan=2)

button_mul = Button(root, text="*", padx=16, pady=10, command=button_mul).grid(row=6, column=0)
button_sub = Button(root, text="-", padx=16, pady=10, command=button_sub).grid(row=6, column=1)
button_div = Button(root, text="/", padx=16, pady=10, command=button_div).grid(row=6, column=2)


root.mainloop()
