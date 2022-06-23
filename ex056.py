print('ANALISANDO DADOS DE PESSOAS')
from datetime import date
somaidade = 0
médiaidande = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for pessoa in range(1,5):
    print('-----------{}ª PESSOA------------'.format(pessoa))
    nome = str(input('Nome:  ')).strip()
    idade = int(input('idade:  '))
    sexo = str(input('Sexo [M/F]:  ')).strip()
    somaidade += idade
    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1


médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('O total de mulheres com menos de 20 anos é de {}'.format(totmulher20))
