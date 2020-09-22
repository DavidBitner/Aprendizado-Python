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
