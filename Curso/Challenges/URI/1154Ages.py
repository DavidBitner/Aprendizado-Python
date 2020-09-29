soma = media = 0
while True:
    n = int(input())
    if n < 0:
        break
    media += n
    soma += 1
media /= soma
print(f"{media:.2f}")
