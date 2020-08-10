def notas(*nota, sit=False):
    """
    Função para analisar notas e situações de vários alunos.
    :param nota: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma.
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
