from tkinter import *
from PIL import ImageTk, Image


def new_window():
    # Caso seja necessário colocar uma imagem em uma nova janela, a variável que controlar a imagem deve ser definida como global
    global my_img
    window = Toplevel()
    my_img = ImageTk.PhotoImage(Image.open("Aula009Imagem1.jpg"))
    Label(window, image=my_img).pack()
    Button(window, text="CLOSE", command=window.destroy).pack()


# Main
root = Tk()
root.title("Doidera")

my_button = Button(root, text="NOVA JANELA", command=new_window).pack()

root.mainloop()
