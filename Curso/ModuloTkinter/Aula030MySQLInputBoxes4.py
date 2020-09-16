from tkinter import *
import mysql.connector

root = Tk()
root.title("Doidera")
root.geometry("400x400+200+200")

# Conectar ao banco
my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="YourPassword",
    database="doidera"
)

# Criar um cursor e inicializa-lo
my_cursor = my_db.cursor()

# Ver o estado da tabela
comando_sql = "SELECT * FROM clientes"
my_cursor.execute(comando_sql)
resultado = my_cursor.fetchall()
for coisa in resultado:
    print(coisa)

root.mainloop()
