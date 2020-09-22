validas = 0
media = 0
while True:
    nota = float(input())
    if nota > 10 or nota < 0:
        print("nota invalida")
    else:
        validas += 1
        media += nota
    if validas == 2:
        break
media /= 2
print(f"media = {media:.2f}")
