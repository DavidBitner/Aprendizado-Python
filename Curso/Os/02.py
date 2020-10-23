import os
from datetime import datetime

# Mostrar varias informações sobre um determinado arquivo
print(os.stat('02.txt'))

# Tamanho do arquivo
tamanho = os.stat('02.txt').st_size
print(tamanho)

# Ultima modificação do arquivo
data_modificacao = os.stat('02.txt').st_mtime
print(datetime.fromtimestamp(data_modificacao))
