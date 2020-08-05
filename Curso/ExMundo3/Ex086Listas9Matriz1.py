matriz = [[], [], []]

for cont1 in range(0, 3):
    for cont2 in range(0, 3):
        n = int(input(f'Digite um valor para [{cont1}, {cont2}]: '))
        matriz[cont1].append(n)

print('-=' * 40)

for cont3 in range(0, 3):
    for cont4 in range(0, 3):
        print(f'[  {matriz[cont3][cont4]:^5}  ]', end=' ')
    print()
