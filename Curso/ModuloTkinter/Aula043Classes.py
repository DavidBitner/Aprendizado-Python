from tkinter import *


def click():
    my_label = Label(root, text="CLICKED BUTTON", font=("Helvetica", 30))
    my_label.pack(padx=10, pady=10)


class Doidera:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.my_button = Button(master, text="CLICK ME", height=2, width=20, command=click)
        self.my_button.pack(padx=10, pady=10)


# Main
root = Tk()
root.title("Doidera")
root.geometry("400x400+200+200")

d = Doidera(root)

root.mainloop()
