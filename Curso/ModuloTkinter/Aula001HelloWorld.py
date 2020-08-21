from tkinter import *

# Sempre começar um programa com o root e a classe Tk
root = Tk()

# Criação do primeiro widget, nesse caso uma label presa a root com o texto "Hello World!"
myLabel = Label(root, text="Hello World!")

# Posicionando a label criada
myLabel.pack()

# Todo programa roda através de um loop, e com o atributo mainloop nós definimos que o programa deixa de rodar a partir desta linha de código. Ou seja, as linhas de código que vierem depois do mainloop serão executadas apenas após o fechamento do gui
root.mainloop()
