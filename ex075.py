print('ANALISE DE UMA TUPLA')
v1 = int(input('Digite o 1º valor: '))
v2 = int(input('Digite o 2º valor: '))
v3 = int(input('Digite o 3º valor: '))
v4 = int(input('Digite o 4º valor: '))
cont = 0
t = (v1, v2, v3, v4)
if v1 == 9:
    cont += 1
if v2 == 9:
    cont += 1
if v3 == 9:
    cont += 1
if v4 == 9:
    cont += 1
print('O valor nove apareceu {} vezes na sequência'.format(cont))
if v1 == 3:
    print('O primeiro valor três aparece na 1ª posição')
if v2 == 3:
    if v1 != 3:
        print('O primeiro valor três apareceu na 2ª posição')
if v3 == 3:
    if v2 != 3:
        if v1 != 3:
            print('O primeiro valor três apareceu na 3ª posição')
if v4 == 3:
    if v3 != 3:
        if v2 != 3:
            if v1 != 3:
                print('O primeiro valor três apareceu na 4ª posição')
print('Os números pares da sequencia são: ')
if v1 % 2 == 0:
    print(v1)
if v2 % 2 == 0:
    print(v2)
if v3 % 2 == 0:
    print(v3)
if v4 % 2 == 0:
    print(v4)


