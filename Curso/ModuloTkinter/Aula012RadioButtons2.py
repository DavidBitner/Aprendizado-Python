from tkinter import *


def clicked():
    r = v.get()
    if r == 0:
        my_label = Label(frame, text="INVALID")
    else:
        my_label = Label(frame, text=f"     {r}     ")
    my_label.grid(row=7, column=0)


root = Tk()
root.title("Doidera")

v = IntVar()
radios = []

frame = LabelFrame(root)
frame.pack(padx=100, pady=100)

for c in range(0, 6):
    radios.append(Radiobutton(frame, text=f"Option {c}", variable=v, value=c, anchor=W))

my_button = Button(frame, text="CLICK ME", padx=5, pady=5, command=clicked)

for c in range(0, len(radios)):
    radios[c].grid(row=c, column=0, sticky=W + E)

my_button.grid(row=6, column=0, padx=50, pady=50)

root.mainloop()
