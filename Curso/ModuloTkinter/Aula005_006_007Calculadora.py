from tkinter import *


def um():
    e.insert(1, "1")


def dois():
    e.insert(1, "2")


def tres():
    e.insert(2, "3")


def quatro():
    e.insert(3, "4")


def cinco():
    e.insert(4, "5")


def seis():
    e.insert(5, "6")


def sete():
    e.insert(6, "7")


def oito():
    e.insert(7, "8")


def nove():
    e.insert(8, "9")


def zero():
    e.insert(9, "0")


def soma():
    base = e.get()
    e.delete(2, "end")
    return base


def clear():
    e.delete(0, "end")


def igual():
    e.insert(10, "=")


# Main
root = Tk()
root.title("Calculadora Simples")

# Caixa de texto
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Definição dos botões
btn_um = Button(root, text="1", width=10, command=um)
btn_dois = Button(root, text="2", width=10, command=dois)
btn_tres = Button(root, text="3", width=10, command=tres)
btn_quatro = Button(root, text="4", width=10, command=quatro)
btn_cinco = Button(root, text="5", width=10, command=cinco)
btn_seis = Button(root, text="6", width=10, command=seis)
btn_sete = Button(root, text="7", width=10, command=sete)
btn_oito = Button(root, text="8", width=10, command=oito)
btn_nove = Button(root, text="9", width=10, command=nove)
btn_zero = Button(root, text="0", width=10, command=zero)
btn_clear = Button(root, text="CLEAR", width=22, command=clear)
btn_mais = Button(root, text="+", width=10, command=soma)
btn_igual = Button(root, text="=", width=22, command=igual)

# Colocar botões na tela
btn_sete.grid(row=1, column=0)
btn_oito.grid(row=1, column=1)
btn_nove.grid(row=1, column=2)
btn_quatro.grid(row=2, column=0)
btn_cinco.grid(row=2, column=1)
btn_seis.grid(row=2, column=2)
btn_um.grid(row=3, column=0)
btn_dois.grid(row=3, column=1)
btn_tres.grid(row=3, column=2)
btn_zero.grid(row=4, column=0)
btn_clear.grid(row=4, column=1, columnspan=2)
btn_mais.grid(row=5, column=0)
btn_igual.grid(row=5, column=1, columnspan=2)

root.mainloop()
