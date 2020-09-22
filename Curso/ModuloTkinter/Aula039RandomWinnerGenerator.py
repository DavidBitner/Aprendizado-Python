from tkinter import *
from random import randint


# Comando do botão que vai sortear o vencedor
def pick_winner():
    global winner_label
    
    # Entradas do sorteio
    entradas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                "u", "u", "v", "w", "x", "y", "z"]

    # Procurar por entrada duplicadas e criar uma lista de entradas unicas
    temp = set(entradas)
    entradas_unicas = list(temp)

    # Realização do sorteio
    numero_de_entradas = len(entradas_unicas)
    vencedor = randint(0, numero_de_entradas - 1)

    # Mostrar vencedor
    winner_label.destroy()
    winner_label = Label(root, text=entradas_unicas[vencedor], font=("Helvetica", 30))
    winner_label.pack(pady=10, padx=10)


# Main
root = Tk()
root.title("Doidera")
root.geometry("400x400+200+200")

winner_label = Label(root)

title_label = Label(root, text="WINNER GENERATOR", font=("Helvetica", 24))
title_label.pack(padx=10, pady=20)

winner_btn = Button(root, text="PICK WINNER", width=20, height=2, command=pick_winner)
winner_btn.pack(pady=20)

root.mainloop()
