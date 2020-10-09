n = int(input())
opcoes = ["tesoura", "papel", "pedra", "lagarto", "Spock"]
prt = 0
for i in range(n):
    escolhas = input().split(" ")
    sheldon = str(escolhas[0])
    raj = str(escolhas[1])
    if sheldon == raj:
        prt = 0
    elif sheldon == opcoes[0] and raj == opcoes[1]:
        prt = 1
    elif sheldon == opcoes[1] and raj == opcoes[2]:
        prt = 1
    elif sheldon == opcoes[2] and raj == opcoes[3]:
        prt = 1
    elif sheldon == opcoes[3] and raj == opcoes[4]:
        prt = 1
    elif sheldon == opcoes[4] and raj == opcoes[0]:
        prt = 1
    elif sheldon == opcoes[0] and raj == opcoes[3]:
        prt = 1
    elif sheldon == opcoes[3] and raj == opcoes[1]:
        prt = 1
    elif sheldon == opcoes[1] and raj == opcoes[4]:
        prt = 1
    elif sheldon == opcoes[4] and raj == opcoes[2]:
        prt = 1
    elif sheldon == opcoes[2] and raj == opcoes[0]:
        prt = 1
    else:
        prt = 2
    if prt == 0:
        print(f"Caso #{i + 1}: De novo!")
    elif prt == 1:
        print(f"Caso #{i + 1}: Bazinga!")
    elif prt == 2:
        print(f"Caso #{i + 1}: Raj trapaceou!")
