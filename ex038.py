print('\033[1;32mComparando Dois Números\033[m')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
if n1 > n2:
    print('O PRIMEIRO número é maior ')
elif n2 > n1:
    print('O SEGUNDO número é maior')
else:
    print('Os números são iguais')
