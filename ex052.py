print('ANALISE DE NÚMEROS PRIMOS')
num = int(input('Digite o número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(' {} '.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num,tot))
if tot == 2:
    print('E por isso É PRIMO !')
else:
    print('E por isso NÃO É PRIMO !')




