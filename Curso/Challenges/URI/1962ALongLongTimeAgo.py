n = int(input())
for i in range(0, n):
    entrada = int(input())
    entrada = 2015 - entrada
    if entrada > 0:
        print(f'{entrada} D.C.')
    elif entrada == 0:
        print('1 A.C.')
    else:
        print(f'{entrada * -1 + 1} A.C.')
