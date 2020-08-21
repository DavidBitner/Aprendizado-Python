from tkinter import *

def myClick():
    myLabel = Label(root, text="CLICKED")
    myLabel.pack()


# Main
root = Tk()

myButton = Button(root, text="CLICK ME", padx="50", pady="50", command=myClick)
myButton.pack()

root.mainloop()
