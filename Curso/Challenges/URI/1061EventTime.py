A, B = input().split(" ")
C, D, E, F, G = input().split(" ")
H, I = input().split(" ")
J, K, L, M, N = input().split(" ")
dia_inicio = int(B)
hora_inicio, minuto_inicio, segundo_inicio = int(C), int(E), int(G)
dia_fim = int(I)
hora_fim, minuto_fim, segundo_fim = int(J), int(L), int(N)
dia_resultado = dia_fim - dia_inicio
if hora_fim < hora_inicio:
    dia_resultado -= 1
    hora_resultado

INCOMPLETO
