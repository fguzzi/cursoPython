sat = float(input('Qual o salário do funcionário: R$ '))
sfi = sat + (sat * 15 / 100)
print('O salário de R$ {:.2f} com 15% de aumento é R$ {:.2f}'.format(sat, sfi))
