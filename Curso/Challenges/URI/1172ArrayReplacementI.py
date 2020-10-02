x = []
for i in range(0, 10):
    x.insert(i, int(input()))
    if x[i] <= 0:
        x[i] = 1
    print(f"X[{i}] = {x[i]}")
