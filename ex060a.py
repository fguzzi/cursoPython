num = int(input('Digite um nº para calcular o fatorial: '))
pr = num
if num == 1 or num == 0:
    print('{}! é igual a 1'.format(num))
else:
    for c in range((num - 1), 0, -1):
        pr = pr * c
    print('{}! é igual a {}'.format(num, pr))
