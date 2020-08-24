from tkinter import *


def button_click(number):
    tela = e.get()
    e.delete(0, END)
    e.insert(0, str(tela) + str(number))


def button_soma():
    base = e.get()
    global soma_num
    global escolha
    soma_num = int(base)
    escolha = "soma"
    e.delete(0, END)


def button_subtracao():
    base = e.get()
    global subtracao_num
    global escolha
    subtracao_num = int(base)
    escolha = "subtracao"
    e.delete(0, END)


def button_divisao():
    base = e.get()
    global divisao_num
    global escolha
    divisao_num = int(base)
    escolha = "divisao"
    e.delete(0, END)


def button_multiplicacao():
    base = e.get()
    global multiplicacao_num
    global escolha
    multiplicacao_num = int(base)
    escolha = "multiplicacao"
    e.delete(0, END)


def clear():
    e.delete(0, END)


def button_equal():
    second = e.get()
    e.delete(0, "end")
    second_num = int(second)
    if escolha in "soma":
        resposta = soma_num + second_num
    elif escolha in "subtracao":
        resposta = subtracao_num - second_num
    elif escolha in "multiplicacao":
        resposta = multiplicacao_num * second_num
    elif escolha in "divisao":
        resposta = divisao_num / second_num
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
btn_clear = Button(root, text="CLEAR", width=33, command=clear)
btn_adicao = Button(root, text="+", width=10, command=button_soma)
btn_subtracao = Button(root, text="-", width=10, command=button_subtracao)
btn_divisao = Button(root, text="/", width=10, command=button_divisao)
btn_multiplicacao = Button(root, text="*", width=10, command=button_multiplicacao)
btn_igual = Button(root, text="=", width=34, command=button_equal)

# Colocar botões na tela
btn_clear.grid(row=1, column=0, columnspan=3)
btn_divisao.grid(row=1, column=3)
btn_sete.grid(row=2, column=0)
btn_oito.grid(row=2, column=1)
btn_nove.grid(row=2, column=2)
btn_multiplicacao.grid(row=2, column=3)
btn_quatro.grid(row=3, column=0)
btn_cinco.grid(row=3, column=1)
btn_seis.grid(row=3, column=2)
btn_subtracao.grid(row=3, column=3)
btn_um.grid(row=4, column=0)
btn_dois.grid(row=4, column=1)
btn_tres.grid(row=4, column=2)
btn_adicao.grid(row=4, column=3)
btn_zero.grid(row=5, column=0)
btn_igual.grid(row=5, column=1, columnspan=3)

root.mainloop()
