lista1 = list(map(int, input().split()))
lista2 = list(map(int, input().split()))
sapo_altura = int(lista1[0])
base = int(lista2[0])
win = True
for i in range(1, len(lista2)):
    if base + sapo_altura < int(lista2[i]) or base - sapo_altura > int(lista2[i]):
        win = False
        break
    base = int(lista2[i])
print('YOU WIN') if win else print('GAME OVER')
