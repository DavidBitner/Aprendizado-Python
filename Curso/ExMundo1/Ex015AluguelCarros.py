dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantidade de Km percorridos: '))
vkm = 0.15 * km
vd = 60 * dias
vt = vd + vkm
print('Total a pagar: R${:.2f}'.format(vt))
