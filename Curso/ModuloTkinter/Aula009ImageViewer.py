from tkinter import *
from PIL import Image, ImageTk


def back():
    global atual
    global my_label
    atual -= 1
    if atual == -1:
        atual = 0
    my_label.grid_forget()
    my_label = Label(image=image_list[atual])
    my_label.grid(row=0, columnspan=3)


def next():
    global atual
    global my_label
    atual += 1
    if atual == len(image_list):
        atual -= 1
    my_label.grid_forget()
    my_label = Label(image=image_list[atual])
    my_label.grid(row=0, columnspan=3)


# Main
atual = 0
root = Tk()
root.title("Doidera")
root.iconbitmap("Aula008icone.ico")

my_img1 = ImageTk.PhotoImage(Image.open("Aula009Imagem1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("Aula009Imagem2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("Aula009Imagem3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("Aula009Imagem4.jpg"))
image_list = [my_img1, my_img2, my_img3, my_img4]
my_label = Label(image=image_list[atual])

button_back = Button(root, text="< -", command=back)
button_next = Button(root, text="- >", command=next)
button_quit = Button(root, text="SAIR", command=root.quit)

my_label.grid(row=0, columnspan=3)
button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_next.grid(row=1, column=2)

root.mainloop()
