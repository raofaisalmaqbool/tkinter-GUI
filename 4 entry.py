from tkinter import *

root = Tk()

# making input field to take input form user
e = Entry(root, width=50, bg="pink", fg="blue", borderwidth=5)
e.pack()
# show some text already in field
e.insert(0, "Enter Some Text")


def myClick():
    # This is fucntion that will call on when myButton will clicked
    var ="Hello " + e.get()
    myLable = Label(root, text=var).pack()


# Make a button widget,,, using colors and using pading,,, callign functions on on click buttion,,, 
myButton = Button(root, text="Click Me!", fg="black", bg="yellow", command=myClick, padx=10, pady=10)
# myButton = Button(root, text="Click Me!", state=DISABLED)

myButton.pack()

root.mainloop()
