from tkinter import *
import mysql.connector

root = Tk()
root.title("Doidera")
root.geometry("400x400+200+200")

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="YourPassword",
)

# Criar um cursor e inicializa-lo
my_cursor = my_db.cursor()

# Criar banco de dados
comando_sql = "CREATE DATABASE doidera"
my_cursor.execute(comando_sql)

root.mainloop()
