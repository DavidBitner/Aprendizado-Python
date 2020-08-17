sacar = float(input('Digite quanto deseja sacar: R$'))
print(f'{sacar // 50:.0f} nota(s) de R$ 50,00')
sacar %= 50
print(f'{sacar // 20:.0f} nota(s) de R$ 20,00')
sacar %= 20
print(f'{sacar // 10:.0f} nota(s) de R$ 10,00')
sacar %= 10
print(f'{sacar:.0f} nota(s) de R$ 1,00')
