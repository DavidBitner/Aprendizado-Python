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

# Alterar colunas na tabela
my_cursor.execute("ALTER TABLE clientes CHANGE first_name primeiro_nome VARCHAR(255)")
my_cursor.execute("ALTER TABLE clientes CHANGE last_name sobrenome VARCHAR(255)")
my_cursor.execute("ALTER TABLE clientes CHANGE zipcode cep INT(10)")
my_cursor.execute("ALTER TABLE clientes CHANGE price_paid valor_pago DECIMAL(10, 2)")

# Ver se a tabela foi modificada corretamente
comando_sql = "SELECT * FROM clientes"
my_cursor.execute(comando_sql)
for coisa in my_cursor.description:
    print(coisa)

root.mainloop()
