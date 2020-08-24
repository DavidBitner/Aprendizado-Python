from tkinter import *


def button_click(number):
    tela = e.get()
    e.delete(0, END)
    e.insert(0, str(tela) + str(number))


def button_soma():
    base = e.get()
    global f_num
    f_num = int(base)
    e.delete(0, "end")


def clear():
    e.delete(0, "end")


def button_equal():
    second = e.get()
    e.delete(0, "end")
    s_num = int(second)
    resposta = f_num + s_num
    e.insert(10, resposta)


# Main
root = Tk()
root.title("Calculadora Simples")

# Caixa de texto
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Definição dos botões
btn_um = Button(root, text="1", width=10, command=lambda: button_click(1))
btn_dois = Button(root, text="2", width=10, command=lambda: button_click(2))
btn_tres = Button(root, text="3", width=10, command=lambda: button_click(3))
btn_quatro = Button(root, text="4", width=10, command=lambda: button_click(4))
btn_cinco = Button(root, text="5", width=10, command=lambda: button_click(5))
btn_seis = Button(root, text="6", width=10, command=lambda: button_click(6))
btn_sete = Button(root, text="7", width=10, command=lambda: button_click(7))
btn_oito = Button(root, text="8", width=10, command=lambda: button_click(8))
btn_nove = Button(root, text="9", width=10, command=lambda: button_click(9))
btn_zero = Button(root, text="0", width=10, command=lambda: button_click(0))
btn_clear = Button(root, text="CLEAR", width=22, command=clear)
btn_mais = Button(root, text="+", width=10, command=button_soma)
btn_igual = Button(root, text="=", width=22, command=button_equal)

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
