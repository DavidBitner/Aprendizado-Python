from tkinter import *


def click(event):
    my_label = Label(root, text="CLICKED")
    my_label.pack()


# Main
root = Tk()
root.title("Doidera")
root.geometry("400x400+200+200")

my_btn = Button(root, text="CLICK ME WITH THE MIDDLE BUTTON", command=click)
my_btn.bind("<Button-2>", click)
my_btn.pack()

root.mainloop()
