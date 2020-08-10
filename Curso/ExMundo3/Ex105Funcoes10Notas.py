def notas(*nota, sit=False):
    """
    Dicionario com as informações de um aluno
    :param nota: Notas do aluno
    :param sit: Parâmetro para apontar se o dicionário terá a situação do aluno
    :return: Um dicionário com a quantidade de notas do aluno, a maior nota, a menor, a média, e caso necessário a situação do aluno.
    """
    dicionario = dict()
    dicionario['total'] = len(nota)
    dicionario['maior'] = max(nota)
    dicionario['menor'] = min(nota)
    dicionario['media'] = sum(nota) / len(nota)
    if sit:
        if dicionario['media'] < 5:
            dicionario['situação'] = 'RUIM'
        elif dicionario['media'] < 7:
            dicionario['situação'] = 'RAZOAVEL'
        else:
            dicionario['situação'] = 'BOA'
    return dicionario


# Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
