A, B = input().split(" ")
a, b = int(A), int(B)
x = 0
if a == b:
    print("O JOGO DUROU 24 HORA(S)")
else:
    if b > a:
        x = b - a
        print(f"O JOGO DUROU {x} HORA(S)")
    elif a > b:
        contador = 0
        tempo = a
        while tempo != b:
            contador += 1
            if tempo == 23:
                tempo = -1
            tempo += 1
        print(f"O JOGO DUROU {contador} HORA(S)")
