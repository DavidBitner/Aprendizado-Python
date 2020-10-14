n = str(input())
negativo = False
if "-" in n:
    negativo = True
entrada = float(n)
if entrada == 0:
    if not negativo:
        print("+", end="")
elif entrada > 0:
    print("+", end="")
print(f"{entrada:.4e}".upper())
