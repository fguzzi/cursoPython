print('CÁLCULO DE GASTOS')
gasto = mil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Produto: ')).strip().upper()
    preco = float(input('Preço em R$: '))
    cont += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [ S/N ]: ')).strip().upper()[0]
    gasto = gasto + preco
    if preco > 1000:
        mil = mil + 1
    if cont == 1 or preco < preco:
        menor = preco
        barato = produto
    if escolha == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print('Total de gastos foi R$ {:.2f}'.format(gasto))
print('Total de produtos com preço superior a R$ 1.000,00 é {}'.format(mil))
print('O produto mais barato é {} que custa R$ {:.2f}'.format(barato, menor))

