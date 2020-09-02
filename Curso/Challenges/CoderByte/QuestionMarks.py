def QuestionsMarks(strParam):
    lista = []
    dados = []
    estado = "false"
    interrogacao = 0
    for c in range(0, len(strParam)):
        if strParam[c].isnumeric():
            dados.append(strParam[c])
            dados.append(c)
            lista.append(dados[:])
            dados.clear()
    for c in range(1, len(lista)):
        if int(lista[c][0]) + int(lista[c - 1][0]) == 10:
            for n in range(lista[c - 1][1], lista[c][1]):
                if strParam[n] in "?":
                    interrogacao += 1
            if interrogacao == 3:
                estado = "true"
                interrogacao = 0
            else:
                estado = "false"
                break
        if estado in "false":
            break
    strParam = estado
    return strParam


# Main
print(QuestionsMarks(str(input())))
