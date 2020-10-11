entrada = input().split(" ")
a, b, c = int(entrada[0]), int(entrada[1]), int(entrada[2])
resposta = ""
if b < a:
    if b < c or b == c:
        resposta = ":)"
    elif b - c < a - b:
        resposta = ":)"
    elif b - c > a - b or b - c == a - b:
        resposta = ":("
elif b > a:
    if b > c or b == c:
        resposta = ":("
    elif c > b:
        resposta = ":)"
        if c - b < b - a:
            resposta = ":("
        elif c - b > b - a:
            resposta = ":)"
elif a == b:
    if b == c:
        resposta = ":("
    if b < c:
        resposta = ":)"
    elif c < b:
        resposta = ":("
print(resposta)
