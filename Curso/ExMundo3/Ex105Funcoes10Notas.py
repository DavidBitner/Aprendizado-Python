def notas(*nota, sit=False):
    dicionario = dict()
    dicionario['total'] = len(nota)
    dicionario['maior'] = max(nota)
    dicionario['menor'] = min(nota)
    dicionario['media'] = sum(nota) / len(nota)
    return dicionario


# Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
