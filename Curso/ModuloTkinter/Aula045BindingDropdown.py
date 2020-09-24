from tkinter import *
from tkinter import ttk


def dropdown_selecionado(event):
    my_label = Label(root, text=selecionado.get())
    my_label.pack()


def combo_box_selecionado(event):
    my_label = Label(root, text=combo_box.get())
    my_label.pack()


# Main
root = Tk()
root.title("Doidera")
root.geometry("400x400+200+200")

opcoes = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

selecionado = StringVar()
selecionado.set(opcoes[0])

dropdown = OptionMenu(root, selecionado, *opcoes, command=dropdown_selecionado)
dropdown.pack(pady=20)

combo_box = ttk.Combobox(root, value=opcoes)
combo_box.current(0)
combo_box.bind("<<ComboboxSelected>>", combo_box_selecionado)
combo_box.pack()

root.mainloop()
