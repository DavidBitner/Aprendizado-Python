n = int(input())
x = []
num = n
for i in range(0, 10):
    x.append(num)
    num += num
    print(f"N[{i}] = {x[i]}")
