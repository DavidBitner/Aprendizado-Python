from tkinter import *


def show():
    Label(root, text=clicked.get()).pack()


# Main
options = ["one", "two", "three", "four", "five", "six", "seven"]

root = Tk()
root.title("Doidera")
root.geometry("400x400+200+200")

clicked = StringVar()
clicked.set("Select a number")

drop = OptionMenu(root, clicked, *options)
drop.pack()

my_btn = Button(root, text="SHOW SELECTION", command=show).pack()

root.mainloop()
