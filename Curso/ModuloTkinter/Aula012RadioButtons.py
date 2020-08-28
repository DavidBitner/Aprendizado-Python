from tkinter import *


def clicked():
    r = v.get()
    if r == 0:
        my_label = Label(frame, text="INVALID")
    else:
        my_label = Label(frame, text=f"     {r}     ")
    my_label.grid(row=3, column=0)


root = Tk()
root.title("Doidera")

frame = LabelFrame(root)
frame.pack()

v = IntVar()

radio1 = Radiobutton(frame, text="Option 1", variable=v, value=1, anchor=W)
radio2 = Radiobutton(frame, text="Option 2", variable=v, value=2, anchor=W)
my_button = Button(frame, text="CLICK ME", padx=5, pady=5, command=clicked)

radio1.grid(row=0, column=0, sticky=W+E)
radio2.grid(row=1, column=0, sticky=W+E)
my_button.grid(row=2, column=0, padx=50, pady=50)

root.mainloop()
