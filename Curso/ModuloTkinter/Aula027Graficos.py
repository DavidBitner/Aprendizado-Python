from tkinter import *
import numpy as np
import matplotlib.pyplot as plt


def grafico():
    precos_casas = np.random.normal(200000, 25000, 5000)
    plt.hist(precos_casas, 50)
    plt.show()
    return


# Main
root = Tk()
root.title("Doidera")
root.geometry("400x400+200+200")

my_btn = Button(root, text="Graficusar", command=grafico)
my_btn.pack()

root.mainloop()
