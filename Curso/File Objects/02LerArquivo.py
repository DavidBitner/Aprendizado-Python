# Armazenar o conteúdo inteiro do documento em uma variável
with open('test.txt', 'r') as f:
    content = f.read()
    print(content)

# Armazenar em uma lista todas as linhas do documento
with open('test.txt', 'r') as f:
    content = f.readlines()
    print(content)

# Armazenar o conteudo de uma linha do documento em uma variável
with open('test.txt', 'r') as f:
    content = f.readline()
    print(content)

# Através do loop for passar por todas as linhas do documento
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end="")
