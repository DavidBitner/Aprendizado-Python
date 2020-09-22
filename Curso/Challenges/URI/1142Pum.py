n = int(input())
pum = 1
for i in range(0, n):
    while True:
        if pum % 4 == 0:
            print("PUM")
            pum += 1
            break
        else:
            print(f"{pum} ", end="")
            pum += 1
