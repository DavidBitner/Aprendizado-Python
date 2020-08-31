from tkinter import *

def slider():
    h = horizontal.get()
    v = vertical.get()
    Label(root, text=h).pack()
    root.geometry(f"{h}x{v}+200+200")


# Main
root = Tk()
root.title("Doidera")
root.geometry(f"400x400+200+200")

vertical = Scale(root, from_=400, to=500)
vertical.pack()

horizontal = Scale(root, from_=400, to=500, orient=HORIZONTAL)
horizontal.pack()

my_btn = Button(root, text="CLICK ME", command=slider).pack()

root.mainloop()
