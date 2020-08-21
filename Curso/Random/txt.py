# Criar e modificar arquivos txt

'''

'r' = Usado somente para ler algo
'w' = Usado somente para escrever algo
'r+' = Usado para ler e escrever algo
'a' = Usado para acrescentar algo

'''

numeros = [0, 15, 10, 20, 15, 45]

# Criar um arquivo e colocar as informações da lista numeros dentro dele
with open('numeros.txt', 'w') as arquivo:
    for numero in numeros:
        arquivo.write(str(f"{numero}\n"))

# Adicionar ao arquivo as informações da lista numeros dentro dele
with open('numeros.txt', 'a') as arquivo:
    for numero in numeros:
        arquivo.write(f'{numero}\n')

# Ler as informações dentro do arquivo de texto
with open('numeros.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)
