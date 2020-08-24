from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Aula008IconesImagens")
root.iconbitmap("Aula008icone.ico")

my_img = ImageTk.PhotoImage(Image.open("Aula008Imagem.png"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="SAIR", command=root.quit)
button_quit.pack()

root.mainloop()
