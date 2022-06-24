def notas(*n, sit=False):
    """        => função para analisar notas de aluno

                 : param n = uma ou mais notas dos alunos; aceita várias
                 : param sit = valor opcional indicando se deve ou não adicionar a situação do aluno
                 : return = retorna um dicionário com as notas
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = "BOA"
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = "RUIM"
    return r


resp = notas(1.5, 8, 3.5, 6, 0.5, sit=True)
print(resp)
help(notas)