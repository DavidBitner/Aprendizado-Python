n = []
g = []
contador = 0
for i in range(20, 0, -1):
    g.append(int(input()))
for i in range(len(g) - 1, -1, -1):
    n.append(g[i])
    print(f"N[{contador}] = {n[contador]}")
    contador += 1
