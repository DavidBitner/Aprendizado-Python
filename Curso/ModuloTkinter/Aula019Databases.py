from tkinter import *
import sqlite3

root = Tk()
root.title("Doidera")
root.geometry("400x400+200+200")

# Criar o banco de dados ou conectar a um
conexao = sqlite3.connect("Aula019...Banco.db")

# Criar cursor
cursor = conexao.cursor()

# Criar tabela
cursor.execute("""CREATE TABLE enderecos (
primeiro_nome text,
sobrenome text,
endereco text,
cidade text,
estado text,
cep integer)""")

# Commitar mudanças
conexao.commit()

# Fechar conexão
conexao.close()

root.mainloop()
