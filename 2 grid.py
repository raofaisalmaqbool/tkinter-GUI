from tkinter import *

root = Tk()

# create a label widget
myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text="                     ").grid(row=1, column=1)
myLabel3 = Label(root, text="My name is Faisal").grid(row=1, column=5)

# showing it into the secreen w.r.t  row and column
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=5)
# myLabel3.grid(row=1, column=5)

root.mainloop()
