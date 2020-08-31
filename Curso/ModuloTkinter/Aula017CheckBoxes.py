from tkinter import *

def check():
    my_label = Label(root, text=variavel.get())
    my_label.pack()


# Main
root = Tk()
root.title("Doidera")
root.geometry("400x400")

variavel = StringVar()

checkbox = Checkbutton(root, text="Check1", variable=variavel, onvalue="On", offvalue="Off")
checkbox.deselect()
checkbox.pack()

my_btn = Button(root, text="CLICK", command=check).pack()

root.mainloop()
