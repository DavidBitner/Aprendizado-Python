inter = gremio = empates = 0
while True:
    A, B = input().split(" ")
    i, g = int(A), int(B)
    if g > i:
        gremio += 1
    elif i > g:
        inter += 1
    else:
        empates += 1
    while True:
        print("Novo grenal (1-sim 2-nao)")
        novo = int(input())
        if novo == 1 or novo == 2:
            break
    if novo == 2:
        break
print(f"{inter + gremio + empates} grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{empates}")
if gremio > inter:
    print("Gremio venceu mais")
elif inter > gremio:
    print("Inter venceu mais")
else:
    print("Nao houve vencedor")
