x = float(input())
n = []
for i in range(0, 100):
    n.append(x)
    print(f"N[{i}] = {n[i]:.4f}")
    x /= 2.0
