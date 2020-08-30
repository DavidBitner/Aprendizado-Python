from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


def open_archive():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="/Curso/ModuloTkinter", title="Escolha um arquivo", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    Label(root, text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    Label(root, image=my_img).pack()


# Main
root = Tk()
root.title("Doidera")

my_btn = Button(root, text="OPEN", command=open_archive).pack()

root.mainloop()
