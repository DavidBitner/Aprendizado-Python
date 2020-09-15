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

# Adicionar colunas a tabela
my_cursor.execute("ALTER TABLE clientes ADD ("
                  "email VARCHAR(255),"
                  "endereco_1 VARCHAR(255),"
                  "endereco_2 VARCHAR(255),"
                  "cidade VARCHAR(50),"
                  "estado VARCHAR(50),"
                  "pais VARCHAR(255),"
                  "telefone VARCHAR(255),"
                  "tipo_de_pagamento VARCHAR(50),"
                  "desconto VARCHAR(255))")

# Ver se a tabela foi criada corretamente
my_cursor.execute("SELECT * FROM clientes")
for coisa in my_cursor.description:
    print(coisa)

root.mainloop()
