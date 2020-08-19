import tkinter as tk  # Importanto a biblioteca tkinter e dando o nome de tk a ela

janela = tk.Tk()
# janela é o nome que está sendo dado a janela principal do programa. tk é a biblioteca tkinter que foi apelidade de tk e está sendo chamada neste comando, Tk é o nome da classe própriamente dita.

janela.title('Janela Principal')
# A função title serve para atribuir um titulo a uma janela, nesse caso está tribuindo o texto "janela principal" a janela com o nome "janela"

janela['bg'] = 'green'
# Atribuindo a cor verde a janela, usando como propriedade "bg".

janela.geometry('300x300+100+100')
# Atribuindo a posição da janela usando como base a string: alturaxaltura+esquerda+topo

janela.mainloop()
# Esse é o comando que faz a execução do programa, sem ele nenhuma janela será aberta.
