resultado = base = 0
valores = input().split(" ")
a = int(valores[0])
ultimo_valor = len(valores) - 1
n = int(valores[ultimo_valor])
for i in range(0, n):
    base += i
    resultado += a
resultado += base
print(resultado)
