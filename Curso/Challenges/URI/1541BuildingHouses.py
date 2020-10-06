while True:
    entrada = input().split(" ")
    a = int(entrada[0])
    if a == 0:
        break
    b, c = int(entrada[1]), int(entrada[2])
    area = a * b
    resposta = area * 100 / c
    resposta **= (1/2)
    print(int(resposta))
