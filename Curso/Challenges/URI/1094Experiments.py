total_cobaias = total_coelhos = total_ratos = total_sapos = 0
entrada = int(input())
for i in range(0, entrada):
    A, B = input().split(" ")
    quantidade, tipo = int(A), str(B)
    if tipo in "C":
        total_coelhos += quantidade
    elif tipo in "S":
        total_sapos += quantidade
    elif tipo in "R":
        total_ratos += quantidade
total_cobaias = total_ratos + total_sapos + total_coelhos
percentual_coelhos = (total_coelhos * 100) / total_cobaias
percentual_ratos = (total_ratos * 100) / total_cobaias
percentual_sapos = (total_sapos * 100) / total_cobaias
print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")
