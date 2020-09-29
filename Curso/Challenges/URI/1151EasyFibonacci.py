n = int(input())
f1 = 0
f2 = 1
f3 = 0
print("0 1", end=" ")
for i in range(0, n - 2):
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print(f3, end="")
    if i < n - 3:
        print(" ", end="")
print()
