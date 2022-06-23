print('ANALISAR SEQUENCIA DE NÚMEROS')
op = 'S'
maior = 0
menor = 0
soma = 0
media = 0
cont = 0
while op == 'S':
    num = int(input('Digite um nº: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma = soma + num
    cont = cont + 1
    media = soma / cont
    op = str(input('Deseja continuar? [S/N] ')).strip().upper()
print(' {} é o maior nº e {} o menor.'.format(maior, menor))
print('A média desses números é {}'.format(media))
