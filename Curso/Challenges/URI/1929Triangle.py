entrada = input().split(" ")
a, b, c, d = int(entrada[0]), int(entrada[1]), int(entrada[2]), int(entrada[3])
resposta = ""
if a + b > c and b + c > a and c + a > b:
    resposta = "S"
elif a + b > d and a + d > b and b + d > a:
    resposta = "S"
elif a + c > d and a + d > c and d + c > a:
    resposta = "S"
elif b + c > d and b + d > c and d + c > b:
    resposta = "S"
else:
    resposta = "N"
print(resposta)
