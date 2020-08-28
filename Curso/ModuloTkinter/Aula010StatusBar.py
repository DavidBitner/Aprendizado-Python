from tkinter import *
from PIL import Image, ImageTk


def back():
    global atual
    global my_label
    global status_label
    atual -= 1
    if atual == -1:
        atual = 0
    my_label.grid_forget()
    my_label = Label(image=image_list[atual])
    my_label.grid(row=0, columnspan=3)
    status_label = Label(root, text=f"Imagem {atual + 1} de {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
    status_label.grid(row=2, column=0, columnspan=3, sticky=W+E)


def next():
    global atual
    global my_label
    global status_label
    atual += 1
    if atual == len(image_list):
        atual -= 1
    my_label.grid_forget()
    my_label = Label(image=image_list[atual])
    my_label.grid(row=0, columnspan=3)
    status_label = Label(root, text=f"Imagem {atual + 1} de {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
    status_label.grid(row=2, column=0, columnspan=3, sticky=W+E)


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
status_label = Label(root, text=f"Imagem {atual + 1} de {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)

button_back = Button(root, text="< -", command=back)
button_next = Button(root, text="- >", command=next)
button_quit = Button(root, text="SAIR", command=root.quit)

my_label.grid(row=0, columnspan=3)
button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_next.grid(row=1, column=2, pady=10)
status_label.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
