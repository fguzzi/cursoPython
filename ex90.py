aluno = dict()
aluno['nome'] = str(input('Digite nome: '))
aluno['media'] = float(input(f' Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situaçao'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'em recuperação'
else:
    aluno['situação'] = 'reprovado'
print()
for k, v in aluno.items():
    print(f' -  {k} é igual a {v}')
