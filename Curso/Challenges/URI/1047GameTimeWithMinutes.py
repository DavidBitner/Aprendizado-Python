A, B, C, D = input().split(" ")
hora_inicial, minuto_inicial, hora_final, minuto_final = int(A), int(B), int(C), int(D)
if hora_inicial == hora_final and minuto_inicial == minuto_final:
    duracao_hora = 24
    duracao_minuto = 0
else:
    duracao_hora = hora_final - hora_inicial
    duracao_minuto = minuto_final - minuto_inicial
    if duracao_hora < 0:
        duracao_hora += 24
    if duracao_minuto < 0:
        duracao_minuto += 60
        duracao_hora -= 1
    if duracao_hora == -1:
        duracao_hora = 23
print(f"O JOGO DUROU {duracao_hora} HORA(S) E {duracao_minuto} MINUTO(S)")
