A, B, C, D = input().split(" ")
n1, n2, n3, n4 = float(A), float(B), float(C), float(D)
estado = str("")
media_final = False
teste = 0
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / (2 + 3 + 4 + 1)
print(f"Media: {media:.1f}")
if media >= 7:
    estado = "Aluno aprovado."
elif media < 5:
    estado = "Aluno reprovado."
else:
    media_final = True
    estado = "Aluno em exame."
    print(f"{estado}")
    teste = float(input())
    print(f"Nota do exame: {teste:.1f}")
    media = (media + teste) / 2
    if media >= 5:
        estado = "Aluno aprovado."
    else:
        estado = "Aluno reprovado."
print(f"{estado}")
if media_final:
    print(f"Media final: {media:.1f}")
