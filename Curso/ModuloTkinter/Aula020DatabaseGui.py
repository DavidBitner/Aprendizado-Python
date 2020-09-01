from tkinter import *
import sqlite3


# Criar função para enviar os dados para a tabela do banco
def enviar():
    conexao = sqlite3.connect("Aula019...Banco.db")
    cursor = conexao.cursor()

    # Insert no banco de dados
    cursor.execute("INSERT INTO enderecos VALUES (:p_nome, :sobrenome, :endereco, :cidade, :estado, :cep)", {
        "p_nome": p_nome.get(),
        "sobrenome": sobrenome.get(),
        "endereco": endereco.get(),
        "cidade": cidade.get(),
        "estado": estado.get(),
        "cep": cep.get()
    })
    conexao.commit()
    conexao.close()

    # Limpar as caixas de texto
    p_nome.delete(0, END)
    sobrenome.delete(0, END)
    endereco.delete(0, END)
    cidade.delete(0, END)
    estado.delete(0, END)
    cep.delete(0, END)


# Criar função para mostrar os dados da tabela na tela
def mostrar():
    conexao = sqlite3.connect("Aula019...Banco.db")
    cursor = conexao.cursor()

    # Mostrar a tabela
    cursor.execute("SELECT *, oid FROM enderecos")
    informacoes = cursor.fetchall()
    mostrar_informacoes = ""
    for informacao in informacoes:
        mostrar_informacoes += f"{informacao[0]} {informacao[1]}\n"
    mostrar_label = Label(root, text=mostrar_informacoes)
    mostrar_label.grid(row=8, column=0, columnspan=2)

    conexao.commit()
    conexao.close()


# Main
root = Tk()
root.title("Doidera")
root.geometry("400x400+200+200")

# Conectar ao banco
conexao = sqlite3.connect("Aula019...Banco.db")
cursor = conexao.cursor()

# Criar labels para os campos de texto
p_nome_label = Label(root, text="Nome", anchor=W)
sobrenome_label = Label(root, text="Sobrenome", anchor=W)
endereco_label = Label(root, text="Endereço", anchor=W)
cidade_label = Label(root, text="Cidade", anchor=W)
estado_label = Label(root, text="Estado", anchor=W)
cep_label = Label(root, text="CEP", anchor=W)

p_nome_label.grid(row=0, column=0, sticky=W + E)
sobrenome_label.grid(row=1, column=0, sticky=W + E)
endereco_label.grid(row=2, column=0, sticky=W + E)
cidade_label.grid(row=3, column=0, sticky=W + E)
estado_label.grid(row=4, column=0, sticky=W + E)
cep_label.grid(row=5, column=0, sticky=W + E)

# Criar caixas de texto
p_nome = Entry(root, width=30)
sobrenome = Entry(root, width=30)
endereco = Entry(root, width=30)
cidade = Entry(root, width=30)
estado = Entry(root, width=30)
cep = Entry(root, width=30)

p_nome.grid(row=0, column=1, padx=20)
sobrenome.grid(row=1, column=1)
endereco.grid(row=2, column=1)
cidade.grid(row=3, column=1)
estado.grid(row=4, column=1)
cep.grid(row=5, column=1)

# Criar botão de enviar
enviar_btn = Button(root, text="ENVIAR", command=enviar)
enviar_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Criar botão de mostrar informações do banco
mostrar_btn = Button(root, text="MOSTRAR", command=mostrar)
mostrar_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=93)

# Commitar para o banco e fechar a conexão
conexao.commit()
conexao.close()
root.mainloop()
