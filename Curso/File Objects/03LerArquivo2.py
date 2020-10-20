# Armazenar em uma variável os 100 primeiros caracteres do documento
with open('test.txt', 'r') as f:
    content = f.read(100)

# Lendo de 10 em 10 caracteres o documento
with open('test.txt', 'r') as f:
    quantidade_caracteres = 10
    conteudo = f.read(quantidade_caracteres)
    while len(conteudo) > 0:
        print(conteudo, end='*')
        conteudo = f.read(quantidade_caracteres)
    print()

# Sabendo a posição do documento em que o script se encontra
with open('test.txt', 'r') as f:
    quantidade_caracteres = 5
    content = f.read(quantidade_caracteres)
    print(content, end='')
    content = f.read(quantidade_caracteres)
    print(content)
    print(f.tell())

# Apontar um lugar especifico do documento para trabalhar
with open('test.txt', 'r') as f:
    quantidade_caracteres = 5
    conteudo = f.read(quantidade_caracteres)
    print(conteudo)
    f.seek(0)
    conteudo = f.read(quantidade_caracteres)
    print(conteudo)
