from ast import Lambda
from sre_parse import State
from tkinter import *
from tkinter.ttk import *
# from PIL import ImageTk, Image

root = Tk()
root.title("Image")

# show image on title side
p1 = PhotoImage(file = 'img/logo.png')
root.iconphoto(False, p1)


# show image on secreen multiple image
my_img_1 = PhotoImage(file = "img/one.jpg")
my_img_2 = PhotoImage(file = "img/two.jpg")
my_img_3 = PhotoImage(file = "img/three.png")

img_list =[my_img_1, my_img_2, my_img_3]   # list to store images

# show image on secreen
my_label = Label(image=my_img_1)           # dont use peak when using grid system
my_label.grid(row=0, column=0, columnspan=3)

def my_function(img_num):
    global my_label
    global forward_Button
    global back_Button

    my_label.grid_forget()   # for remove the present image from secren
    my_label = Label(image=img_list[img_num-1])   # show the next image in secreen
    forward_Button = Button(root, text=">>", command=lambda: my_function(img_num+1))   # it recall the forward function
    back_Button = Button(root, text="<<", command=lambda: my_function(img_num-1)) # it will call the back function and control goes to the back fucntion

    if img_num == len(img_list):           # it will compair the length of list 
        forward_Button = Button(root, text=">>", state=DISABLED)

    if img_num == 1:
        back_Button = Button(root, text="<<", state=DISABLED)

    # placement of image and button on secren by grid system
    my_label.grid(row=0, column=0, columnspan=3)    
    forward_Button.grid(row=1, column=2)
    back_Button.grid(row=1, column=0)
     

# def back(img_num):
#     global my_label
#     global forward_Button
#     global back_Button

#     my_label.grid_forget()   # for remove the present image from secren
#     my_label = Label(image=img_list[img_num-1])
#     forward_Button = Button(root, text=">>", command=lambda: forward(img_num+1))
#     back_Button = Button(root, text="<<", command=lambda: back(img_num-1))

#     if img_num == 1:
#         back_Button = Button(root, text="<<", state=DISABLED)

#     my_label.grid(row=0, column=0, columnspan=3)
#     forward_Button.grid(row=1, column=2)
#     back_Button.grid(row=1, column=0)



# # create a label widget
back_Button = Button(root, text="<<", state=DISABLED)
exit_Button = Button(root, text="Exit Program", command=root.quit)   # this exit the system 
forward_Button = Button(root, text=">>", command=lambda: my_function(2))

# showing it into the secreen
# myButton.pack()
back_Button.grid(row=1, column=0)
exit_Button.grid(row=1, column=1)
forward_Button.grid(row=1, column=2)

root.mainloop()
