from tkinter import *


def command():
    return


def file_new():
    file_new_frame.pack(fill="both", expand=1)


# Main
root = Tk()
root.title("Doidera")
root.geometry("400x400+200+200")

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(Label="File", menu=file_menu)
file_menu.add_command(Label="New...", command=file_new)
file_menu.add_separator()
file_menu.add_command(Label="Exit", command=root.quit)

file_new_frame = Frame(root, width=400, height=400)

edit_menu = Menu(my_menu)
my_menu.add_cascade(Label="Edit", menu=file_menu)
file_menu.add_command(Label="Cut", command=command)
file_menu.add_separator()
file_menu.add_command(Label="Cut", command=command)

view_menu = Menu(my_menu)
my_menu.add_cascade(Label="View", menu=file_menu)
file_menu.add_command(Label="Recent Files", command=command)
file_menu.add_separator()
file_menu.add_command(Label="Type Info", command=command)

root.mainloop()
