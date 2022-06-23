print('ANALISANDO UMA LISTA DE PESSOAS')
maior = 0
hom = 0
mul20 = 0
while True:
    print('CADASTRE UMA PESSOA')
    print('-'*37)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [ M / F ]: ')).strip().upper()[0]
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [ S / N ]: ')).strip().upper()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        hom += 1
    if sexo == 'F' and idade < 20:
        mul20 += 1
    if escolha == 'N':
        break
print('{} pessoas são maiores de 18 anos'.format(maior))
print('{} pessoas são do sexo masculino'.format(hom))
print('{} mulheres tem menos de 20 anos'.format(mul20))
