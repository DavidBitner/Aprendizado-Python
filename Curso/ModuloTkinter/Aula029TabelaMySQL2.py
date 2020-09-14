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

# Ver se o banco de dados foi criado
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)

root.mainloop()
