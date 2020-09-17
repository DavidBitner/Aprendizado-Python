from tkinter import *


# Comando do botão hello
def hello_world():
    global hello_label
    hello_label.destroy()
    texto = f"Hello {name_entry.get()}"
    hello_label = Label(root, text=texto)
    hello_label.grid(row=3, column=0)


# Main
root = Tk()
root.title("doidera")
root.geometry("400x400")

hello_label = Label(root)

name_entry = Entry(root, font=("Helvetica", 30))
name_entry.grid(row=0, column=0)

hello_btn = Button(root, text="HELLO", command=hello_world, height=2, width=20)
hello_btn.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()
