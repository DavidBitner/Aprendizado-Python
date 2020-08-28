from tkinter import *

root = Tk()
root.title("Doidera")

frame = LabelFrame(root, text="This is my frame...", padx=5, pady=5)
frame.pack(padx=100, pady=100)

my_button1 = Button(frame, text="DON'T CLICK HERE")
my_button2 = Button(frame, text="UAU")

my_button1.grid(row=0, column=0)
my_button2.grid(row=1, column=1)

root.mainloop()
