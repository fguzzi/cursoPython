print('-' * 40)
print('{:^30}'.format('CAIXA ELETRONICO'))
print('-' * 40)
ced50 = 0
ced20 = 0
ced10 = 0
ced1 = 0
q = int(input('Qual o valor do saque? R$ '))
ced50 = q // 50
ced20 = (q % 50) // 20
ced10 = ((q % 50) % 20) // 10
ced1 = (((q % 50) % 20) % 10) // 1
if ced50 > 0:
    print('{} cédulas de R$ 50.00'.format(ced50))
if ced20 > 0:
    print('{} cédulas de R$ 20.00'.format(ced20))
if ced10 > 0:
    print('{} cédulas de R$ 10.00'.format(ced10))
if ced1 > 0:
    print('{} cédulas de R$ 1.00'.format(ced1))

