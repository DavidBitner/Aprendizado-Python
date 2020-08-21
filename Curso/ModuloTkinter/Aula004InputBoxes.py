from tkinter import *

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


# Main
root = Tk()

e = Entry(root, width=50)
e.pack()
e.get()
e.insert(0, "Enter your name: ")

myButton = Button(root, text="CLICK ME", padx="50", pady="10", command=myClick)
myButton.pack()

root.mainloop()
