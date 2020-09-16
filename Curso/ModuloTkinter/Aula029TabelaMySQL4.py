from tkinter import *
import mysql.connector

root = Tk()
root.title("Doidera")
root.geometry("400x400+200+200")

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="YourPassword",
    database="doidera"
)

# Criar um cursor e inicializa-lo
my_cursor = my_db.cursor()

# Ver se a tabela foi criada
comando_sql = "SELECT * FROM clientes"
my_cursor.execute(comando_sql)
for coisa in my_cursor.description:
    print(coisa)

root.mainloop()
