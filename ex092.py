print('DADOS CTPS')
from datetime import date
nome = str(input('Nome: '))
dn = int(input('Ano de nascimento: '))
ctps = str(input('Carteira de trabalhao [ 0 não tem]: '))
if ctps != 0:
    contratacao = int(input('Ano de contrataçao: '))
    salario = float(input('Salário: '))
idade = date.today().year - dn
aposentadoria = (contratacao + 35) - dn
dados = {'Nome': nome, 'Idade': idade, 'Carteira de trabalho': ctps, 'Contratação': contratacao, 'Salário': salario, 'Aposentadoria': aposentadoria}
print(f' Nome tem valor {nome}', end=' ')
print()
print(f' Idade tem valor {idade}', end=' ')
print()
print(f' Ctps é {ctps}', end=' ')
print()
print(f' Contratação tem o valor {contratacao}', end=' ')
print()
print(f' Salário tem o valor R$ {salario: .2f}', end=' ')
print()
print(f' Aposentadoria tem o valor {aposentadoria}')
