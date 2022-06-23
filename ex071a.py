print('-' * 40)
print('{:^30}'.format('CAIXA ELETRONICO'))
print('-' * 40)
valor = int(input('Qual valor você deseja sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print('Total de {} cédulas de R$ {}'.format(totced, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('-' * 40)
print('Volte sempre ao Caixa Eletrônico')






