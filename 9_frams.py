from tkinter import *
from tkinter.ttk import *
# from PIL import ImageTk, Image

root = Tk()
root.title("Image")


# show image on title side
p1 = PhotoImage(file = 'img/logo.png')
root.iconphoto(False, p1)
 

frame = LabelFrame(root, text="this is window")
frame.pack(padx=50, pady=50)

b1 = Button(frame, text="button 1") # button 1 show inside the frame
b1.grid(row=0, column=0)                       

b2 = Button(frame, text="button 2")  # buttion 2 show inside the frame
b2.grid(row=1, column=1)

root.mainloop()
