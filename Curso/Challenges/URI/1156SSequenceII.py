s = 1
base = 2
for i in range(3, 40, 2):
    s = s + i / base
    base *= 2
print(f"{s:.2f}")
