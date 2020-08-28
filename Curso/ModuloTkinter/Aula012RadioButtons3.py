from tkinter import *


def clicked():
    r = pizza.get()
    if r in "":
        my_label = Label(frame, text="INVALID")
    else:
        my_label = Label(frame, text=f"     {r}      ")
    my_label.grid(row=7, column=0)


root = Tk()
root.title("Doidera")

pizza = StringVar()
radios = []
sabores = ["Queijo", "Peperoni", "Chocolate", "Azeitona"]

frame = LabelFrame(root)
frame.pack(padx=100, pady=100)

for text in sabores:
    radios.append(Radiobutton(frame, text=text, variable=pizza, value=text, anchor=W))

my_button = Button(frame, text="CLICK ME", padx=5, pady=5, command=clicked)

for c in range(0, len(radios)):
    radios[c].grid(row=c, column=0, sticky=W + E)
my_button.grid(row=6, column=0, padx=50, pady=50)

root.mainloop()
