from tkinter import *

root = Tk()

def myClick():
    # This is fucntion that will call on when myButton will clicked
    myLable = Label(root, text="My name is Faisal").pack()

# Make a button widget,,, using colors and using pading,,, callign functions on on click buttion,,, 
myButton = Button(root, text="Click Me!", fg="black", bg="yellow", command=myClick, padx=20, pady=20)
# myButton = Button(root, text="Click Me!", state=DISABLED)

myButton.pack()

root.mainloop()
