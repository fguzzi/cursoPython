print('{:=^40}'.format(' BAÚ DA FELICIDADE '))
print('\033[4;34mCalcular Preço\033[m')
pre = float(input('Digite o preço do produto: R$ '))
print('''Condições de Pagamento: 
[ 1 ] - à vista  
[ 2 ] - à vista no cartão
[ 3 ] - 2x no cartão
[ 4 ] - 3x ou mais no cartão''')
escolha = int(input('Digite sua escolha: '))
if escolha == 1:
    total = (pre) - (pre * 10 / 100)
elif escolha == 2:
    total = (pre) - (pre * 5 / 100)
elif escolha == 3:
    total = pre
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} sem juros'.format(parcela))
elif escolha == 4:
    total = (pre) + (pre * 20 /100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} com juros'.format(totparc, parcela))
else:
    total = pre
    print('CONDIÇÃO INVÁLIDA de pagamento. Tente novamente.')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(pre, total))
