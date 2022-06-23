km = float(input('Qual a distância em km de sua viagem? '))
if km <= 200:
    print('O custo da viagem é R$ {:.2f}'.format(km * 0.50))
else:
    print('O custo da viagem é R$ {:.2f}'.format(km * 0.45))

