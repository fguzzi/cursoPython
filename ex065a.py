print('ANALISAR SEQUENCIA DE NÚMEROS')
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um nº: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N] ')).strip()[0].upper()
media = soma / quant
print('Você digitou {} números e a média é {}'.format(quant, media))
print('{} é o maior número e {} é o menor'.format(maior,menor))
