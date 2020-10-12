n = int(input())
for i in range(0, n):
    prt = ""
    nomes_escolhas = input().split(" ")
    numeros_escolhas = input().split(" ")
    nome1, escolha1, nome2, escolha2 = str(nomes_escolhas[0]), str(nomes_escolhas[1]), str(nomes_escolhas[2]), \
                                       str(nomes_escolhas[3])
    numero1, numero2 = int(numeros_escolhas[0]), int(numeros_escolhas[1])
    resultado = numero1 + numero2
    if resultado % 2 == 0:
        resposta = "PAR"
    else:
        resposta = "IMPAR"
    if resposta == "PAR":
        if escolha1 == "PAR":
            prt = nome1
        elif escolha2 == "PAR":
            prt = nome2
    elif resposta == "IMPAR":
        if escolha1 == "IMPAR":
            prt = nome1
        elif escolha2 == "IMPAR":
            prt = nome2
    print(prt)
