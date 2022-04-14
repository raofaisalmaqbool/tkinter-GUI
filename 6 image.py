from tkinter import *
from tkinter.ttk import *
# from PIL import ImageTk, Image

root = Tk()
root.title("Image")

# show image on title side
p1 = PhotoImage(file = 'img/logo.png')
root.iconphoto(False, p1)


# show image on secreen
my_image = PhotoImage(file = "img/logo.png")
myLabel = Label(image=my_image)
myLabel.pack()


# create a label widget
myButton = Button(root, text="Exit Program", command=root.quit)

# showing it into the secreen
myButton.pack()

root.mainloop()
