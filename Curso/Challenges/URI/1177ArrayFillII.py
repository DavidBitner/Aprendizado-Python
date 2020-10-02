t = int(input())
base = 0
n = []
for i in range(0, 1000):
    n.append(base)
    base += 1
    if base == t:
        base = 0
    print(f"N[{i}] = {n[i]}")
