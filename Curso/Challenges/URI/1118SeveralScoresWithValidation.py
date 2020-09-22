media = validas = 0
while True:
    nota = float(input())
    if nota > 10 or nota < 0:
        print("nota invalida")
    else:
        media += nota
        validas += 1
    if validas == 2:
        media /= 2
        print(f"media = {media:.2f}")
        validas = 0
        media = 0
        while True:
            print("novo calculo (1-sim 2-nao)")
            novo = int(input())
            if novo == 1 or novo == 2:
                break
        if novo == 2:
            break
