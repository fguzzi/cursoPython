km = float(input('Qual a distância em km de sua viagem? '))
preco = km * 0.50 if km <= 200 else km * 0.45
print('O preço de sua passagem é R$ {:.2f}'.format(preco))

