from tkinter import *
import sqlite3


# Criar função para enviar os dados para a tabela do banco
def enviar():
    # Conectar com o banco
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

    # Fechar conexão com o banco
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
    # Conectar ao banco
    conexao = sqlite3.connect("Aula019...Banco.db")
    cursor = conexao.cursor()

    # Mostrar a tabela
    cursor.execute("SELECT *, oid FROM enderecos")
    informacoes = cursor.fetchall()
    mostrar_informacoes = "" * 50
    for informacao in informacoes:
        mostrar_informacoes += f"{informacao[0]} {informacao[1]} {informacao[6]}\n"
    mostrar_label = Label(root, text=mostrar_informacoes)
    mostrar_label.grid(row=11, column=0, columnspan=2)

    # Fechar conexão com o banco
    conexao.commit()
    conexao.close()


# Criar função para deletar valores do banco
def deletar():
    # Conectar ao banco
    conexao = sqlite3.connect("Aula019...Banco.db")
    cursor = conexao.cursor()

    # Deletar do banco
    cursor.execute(f"DELETE FROM enderecos WHERE oid='{id_campo.get()}';")

    # Fechar conexão com o banco
    conexao.commit()
    conexao.close()


# Criar função do botão de edição
def editar():
    # Conectar ao banco
    conexao = sqlite3.connect("Aula019...Banco.db")
    cursor = conexao.cursor()

    id_selecionado = id_campo.get()

    # Atualização
    cursor.execute("""UPDATE enderecos SET
    primeiro_nome = :nome,
    sobrenome = :sobrenome,
    endereco = :endereco,
    cidade = :cidade,
    estado = :estado,
    cep = :cep 
    WHERE oid = :oid""", {"nome": p_nome_att.get(),
                          "sobrenome": sobrenome_att.get(),
                          "endereco": endereco_att.get(),
                          "cidade": cidade_att.get(),
                          "estado": estado_att.get(),
                          "cep": cep_att.get(),
                          "oid": id_selecionado})

    # Fechar conexão com o banco
    conexao.commit()
    conexao.close()
    att.destroy()


# Criar função de atualizar de valores
def atualizar():
    # Conectar ao banco
    conexao = sqlite3.connect("Aula019...Banco.db")
    cursor = conexao.cursor()

    id_selecionado = id_campo.get()
    # Selecionar no banco
    cursor.execute(f"SELECT * FROM enderecos WHERE oid = {id_selecionado}")
    dados = cursor.fetchall()

    # Criar nova janela
    global att
    att = Tk()
    att.title("Atualizar")
    att.geometry("300x300+400+400")

    # Criar labels para os campos de texto
    p_nome_label_att = Label(att, text="Nome", anchor=W)
    sobrenome_label_att = Label(att, text="Sobrenome", anchor=W)
    endereco_label_att = Label(att, text="Endereço", anchor=W)
    cidade_label_att = Label(att, text="Cidade", anchor=W)
    estado_label_att = Label(att, text="Estado", anchor=W)
    cep_label_att = Label(att, text="CEP", anchor=W)
    p_nome_label_att.grid(row=0, column=0, sticky=W + E)
    sobrenome_label_att.grid(row=1, column=0, sticky=W + E)
    endereco_label_att.grid(row=2, column=0, sticky=W + E)
    cidade_label_att.grid(row=3, column=0, sticky=W + E)
    estado_label_att.grid(row=4, column=0, sticky=W + E)
    cep_label_att.grid(row=5, column=0, sticky=W + E)

    # Criar variáveis globais para as caixas de texto
    global p_nome_att
    global sobrenome_att
    global endereco_att
    global cidade_att
    global estado_att
    global cep_att

    # Criar caixas de texto
    p_nome_att = Entry(att, width=30)
    sobrenome_att = Entry(att, width=30)
    endereco_att = Entry(att, width=30)
    cidade_att = Entry(att, width=30)
    estado_att = Entry(att, width=30)
    cep_att = Entry(att, width=30)
    p_nome_att.grid(row=0, column=1, padx=20)
    sobrenome_att.grid(row=1, column=1)
    endereco_att.grid(row=2, column=1)
    cidade_att.grid(row=3, column=1)
    estado_att.grid(row=4, column=1)
    cep_att.grid(row=5, column=1)

    # Loop pelos dados
    for dado in dados:
        p_nome_att.insert(0, dado[0])
        sobrenome_att.insert(0, dado[1])
        endereco_att.insert(0, dado[2])
        cidade_att.insert(0, dado[3])
        estado_att.insert(0, dado[4])
        cep_att.insert(0, dado[5])

    # Criar botão para salvar
    salvar_btn = Button(att, text="SALVAR", command=editar)
    salvar_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=99)

    # Fechar conexão com o banco
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

# Criar botão para deletar informações do banco
del_btn = Button(root, text="DELETAR", command=deletar)
del_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=98)

# Criar espaço para selecionar o id
id_label = Label(root, text="Selecionar ID", anchor=W)
id_campo = Entry(root, width=30)
id_label.grid(row=9, column=0, sticky=W + E)
id_campo.grid(row=9, column=1)

# Criar botão para atualizar informações no banco
att_btn = Button(root, text="ATUALIZAR", command=atualizar)
att_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=91)

# Commitar para o banco e fechar a conexão
conexao.commit()
conexao.close()
root.mainloop()
