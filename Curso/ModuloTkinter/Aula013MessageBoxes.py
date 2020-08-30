from tkinter import *
from tkinter import messagebox


def popup():
    resposta = messagebox.askyesno("Popup", "This is a popup")
    if resposta == 1:
        my_label = Label(root, text="Você escolheu sim")
    else:
        my_label = Label(root, text="Você escolheu não")
    my_label.pack()


root = Tk()
root.title("Doidera")

my_button = Button(root, text="popup", command=popup).pack()

root.mainloop()
