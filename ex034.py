print('Cálculo de aumento de salário.')
sa = float(input('Digite o salário do funcionário: R$ '))
if sa > 1250:
    print('O salário com 10% de aumento será R$ {:.2f}'.format(sa + (sa * 10 / 100)))
else:
    print('O salário com 15% de aumento será R$ {:.2f}'.format(sa + (sa * 15 / 100)))
