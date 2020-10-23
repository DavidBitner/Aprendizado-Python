import os

# Get current working directory ou, mostrar o diretório atual que está sendo utilizado
print(os.getcwd())

# Change directory ou, mudar o diretório em que se está trabalhando
os.chdir('C:/Users/David/Documents/GitHub/Aprendizado-Python/Curso/os')

# List directory ou, mostrar o que se encontra dentro do diretório que está sendo utilizado
print(os.listdir())

# Make directory ou, criar uma pasta no diretório que está sendo utilizado
os.mkdir('Test')

# Make directories ou, criar toda a cadeia de arquivos necessários
os.makedirs('test2/test')

# Renomear arquivos
os.rename('Test', 'demo')

# Remove directory ou, remover a pasta
os.rmdir('demo')

# Remove directories ou, remover toda a cadeia de pastas
os.removedirs('test2/test')
