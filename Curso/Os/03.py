import os

os.chdir('/Users/David/Desktop/')

# os.walk() é uma função que serve para mostrar tudo que se encontra dentro de um diretório
for dirpath, dirnames, filenames in os.walk('/Users/David/Desktop/entertainment'):
    print('Current Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()
