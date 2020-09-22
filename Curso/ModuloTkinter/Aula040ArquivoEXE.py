# Para se criar um arquivo .EXE, deve-se primeiro ter o pyinstaller
# Segundo deve-se ter todos os pacotes do código instalados corretamente no diretório do código
# Terceiro deve-se ir até o terminal e digitar o seguinte código:
# pyinstaller.exe --onefile --windowed nome_do_arquivo.py
# one file é o comando para criar o exe com apenas um arquivo, windowed serve para que o console não apareça quando o
# exe for executado
# Importante: Caso o exe não esteja funcionando corretamente, deve-se deletar os arquivos criados pelo pyinstaller, e
# refazer o comando sem a parte "--windowed", assim o terminal será aberto junto com o exe na hora de executar o
# arquivo e assim se ocorrer algum erro no funcionamento do programa, o terminal irá apontar qual o erro

from tkinter import *


# Comando do botão hello
def hello_world():
    global hello_label
    texto = f"Hello {name_entry.get()}"
    hello_label = Label(root, text=texto)
    hello_label.pack()
    hello_btn['state'] = DISABLED


# Comando do botão delete
def delete():
    hello_label.pack_forget()
    hello_btn['state'] = NORMAL


# Main
root = Tk()
root.title("doidera")
root.geometry("400x400")

name_entry = Entry(root, font=("Helvetica", 30), width=50)
name_entry.pack(padx=10, pady=10)

hello_btn = Button(root, text="HELLO", command=hello_world, height=2, width=20)
hello_btn.pack(padx=10, pady=10)

root.mainloop()
