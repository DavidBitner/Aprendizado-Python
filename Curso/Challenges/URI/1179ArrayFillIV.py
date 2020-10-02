par = []
impar = []
for i in range(0, 15):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    if len(par) == 5:
        for c in range(0, 5):
            print(f"par[{c}] = {par[c]}")
        par = []
    if len(impar) == 5:
        for c in range(0, 5):
            print(f"impar[{c}] = {impar[c]}")
        impar = []
for c in range(0, len(impar)):
    print(f"impar[{c}] = {impar[c]}")
for c in range(0, len(par)):
    print(f"par[{c}] = {par[c]}")
