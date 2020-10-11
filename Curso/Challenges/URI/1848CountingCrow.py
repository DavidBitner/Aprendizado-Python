grito = soma = 0
while grito < 3:
    entrada = str(input())
    if entrada in "caw caw":
        grito += 1
        print(soma)
        soma = 0
    elif entrada in "--*":
        soma += 1
    elif entrada in "-*-":
        soma += 2
    elif entrada in "-**":
        soma += 3
    elif entrada in "*--":
        soma += 4
    elif entrada in "*-*":
        soma += 5
    elif entrada in "**-":
        soma += 6
    elif entrada in "***":
        soma += 7
