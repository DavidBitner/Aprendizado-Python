from tkinter import *
import mysql.connector
import csv


# Funções
# Função do botão de limpar campos
def limpar_campos():
    primeiro_nome_entry.delete(0, END)
    sobrenome_entry.delete(0, END)
    endereco_1_entry.delete(0, END)
    endereco_2_entry.delete(0, END)
    cidade_entry.delete(0, END)
    estado_entry.delete(0, END)
    cep_entry.delete(0, END)
    pais_entry.delete(0, END)
    telefone_entry.delete(0, END)
    email_entry.delete(0, END)
    tipo_de_pagamento_entry.delete(0, END)
    desconto_entry.delete(0, END)
    valor_pago_entry.delete(0, END)


# Função do botão de adicionar clientes ao banco
def adicionar_cliente():
    # Comando sql para inserir os dados dos campos de texto dentro do banco
    comando_sql = f"INSERT INTO clientes (primeiro_nome, sobrenome, cep, valor_pago, email, endereco_1, endereco_2, " \
                  f"cidade, estado, pais, telefone, tipo_de_pagamento, desconto) VALUES (" \
                  f"'{primeiro_nome_entry.get()}', '{sobrenome_entry.get()}', {cep_entry.get()}, " \
                  f"{valor_pago_entry.get()}, '{email_entry.get()}', '{endereco_1_entry.get()}', " \
                  f"'{endereco_2_entry.get()}', '{cidade_entry.get()}', '{estado_entry.get()}', " \
                  f"'{pais_entry.get()}', {telefone_entry.get()}, '{tipo_de_pagamento_entry.get()}', " \
                  f"{desconto_entry.get()})"
    my_cursor.execute(comando_sql)

    # Commitar as mudanças para o banco
    my_db.commit()

    # Limpar os campos de texto
    limpar_campos()


# Função do botão de exportar tabela para o Excel
def exportar_para_excel(resultado):
    with open("clientes.csv", "w") as tabela:
        escrever = csv.writer(tabela, dialect='excel')
        for coisa in resultado:
            escrever.writerow(coisa)


# Função do botão listar clientes
def listar_clientes():
    global i
    listar_clientes_window = Tk()
    listar_clientes_window.title("Listar Clientes")
    listar_clientes_window.geometry("800x600")

    # Listar o que há dentro da tabela
    comando_sql = "SELECT * FROM clientes"
    my_cursor.execute(comando_sql)
    resultado = my_cursor.fetchall()
    for i, coisa in enumerate(resultado):
        coluna = 0
        for c in coisa:
            cliente_label = Label(listar_clientes_window, text=c)
            cliente_label.grid(row=i + 1, column=coluna)
            coluna += 1

    # Opção de exportar tabela para o Excel
    excel_btn = Button(listar_clientes_window, text="EXPORTAR PARA EXCEL", height=2, width=20,
                       command=lambda: exportar_para_excel(resultado))
    excel_btn.grid(row=i + 2, column=0, columnspan=14)


# Main
root = Tk()
root.title("Doidera")
root.geometry("400x600+200+200")

# Conectar ao banco
my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="YourPassword",
    database="doidera"
)

# Criar um cursor e inicializa-lo
my_cursor = my_db.cursor()

# Titulo da interface
titulo_label = Label(root, text="Cadastro Clientes", font=("Helvetica", 30))
titulo_label.grid(row=0, column=0, columnspan=2)

# Labels dos campos de cadastro
primeiro_nome_label = Label(root, text="Primeiro Nome")
sobrenome_label = Label(root, text="Sobrenome")
cep_label = Label(root, text="Cep")
valor_pago_label = Label(root, text="Valor Pago")
email_label = Label(root, text="Email")
endereco_1_label = Label(root, text="Endereço 1")
endereco_2_label = Label(root, text="Endereço 2")
cidade_label = Label(root, text="Cidade")
estado_label = Label(root, text="Estado")
pais_label = Label(root, text="País")
telefone_label = Label(root, text="Telefone")
tipo_de_pagamento_label = Label(root, text="Tipo de pagamento")
desconto_label = Label(root, text="Desconto")

# Posicionamento das labels na interface
primeiro_nome_label.grid(row=1, column=0, sticky=W, padx=10)
sobrenome_label.grid(row=2, column=0, sticky=W, padx=10)
endereco_1_label.grid(row=3, column=0, sticky=W, padx=10)
endereco_2_label.grid(row=4, column=0, sticky=W, padx=10)
cidade_label.grid(row=5, column=0, sticky=W, padx=10)
estado_label.grid(row=6, column=0, sticky=W, padx=10)
cep_label.grid(row=7, column=0, sticky=W, padx=10)
pais_label.grid(row=8, column=0, sticky=W, padx=10)
telefone_label.grid(row=9, column=0, sticky=W, padx=10)
email_label.grid(row=10, column=0, sticky=W, padx=10)
tipo_de_pagamento_label.grid(row=11, column=0, sticky=W, padx=10)
desconto_label.grid(row=12, column=0, sticky=W, padx=10)
valor_pago_label.grid(row=13, column=0, sticky=W, padx=10)

# Campos de Texto
primeiro_nome_entry = Entry(root)
sobrenome_entry = Entry(root)
endereco_1_entry = Entry(root)
endereco_2_entry = Entry(root)
cidade_entry = Entry(root)
estado_entry = Entry(root)
cep_entry = Entry(root)
pais_entry = Entry(root)
telefone_entry = Entry(root)
email_entry = Entry(root)
tipo_de_pagamento_entry = Entry(root)
desconto_entry = Entry(root)
valor_pago_entry = Entry(root)

# Posicionando campos de texto
primeiro_nome_entry.grid(row=1, column=1)
sobrenome_entry.grid(row=2, column=1)
endereco_1_entry.grid(row=3, column=1)
endereco_2_entry.grid(row=4, column=1)
cidade_entry.grid(row=5, column=1)
estado_entry.grid(row=6, column=1)
cep_entry.grid(row=7, column=1)
pais_entry.grid(row=8, column=1)
telefone_entry.grid(row=9, column=1)
email_entry.grid(row=10, column=1)
tipo_de_pagamento_entry.grid(row=11, column=1)
desconto_entry.grid(row=12, column=1)
valor_pago_entry.grid(row=13, column=1)

# Criar botões
adicionar_btn = Button(root, text="ADICIONAR", command=adicionar_cliente, height=2, width=20)
limpar_btn = Button(root, text="LIMPAR", command=limpar_campos, height=2, width=20)
listar_clientes_btn = Button(root, text="LISTAR", height=2, width=20, command=listar_clientes)

# Posicionar botões
adicionar_btn.grid(row=14, column=0, padx=10, pady=10)
limpar_btn.grid(row=14, column=1, padx=10, pady=10)
listar_clientes_btn.grid(row=15, column=0, padx=10, sticky=W)

root.mainloop()
