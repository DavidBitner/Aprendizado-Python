def BracketMatcher(strParam):
    abre_parenteses = 0
    fecha_parenteses = 0
    primeiro = False
    expressao = strParam
    for c in expressao:
        if c in '(':
            break
        if c in ')':
            primeiro = True
            break
    if not primeiro:
        for c in expressao:
            if c in '(':
                abre_parenteses += 1
            if c in ')':
                fecha_parenteses += 1
            if fecha_parenteses > abre_parenteses:
                break
    if primeiro or abre_parenteses != fecha_parenteses:
        strParam = "0"
    else:
        strParam = "1"
    return strParam


# Main
print(BracketMatcher(input()))
