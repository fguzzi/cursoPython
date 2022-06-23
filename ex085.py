print('LISTA NUMEROS PARES E LISTA DE NUMEROS IMPARES')
geral = list()
pares = list()
impares = list()
geral.append([pares])
geral.append([impares])
for cont in range(0, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f' A lista completa é {geral}')
print(f' Os números pares são {sorted(pares)}')
print(f' Os números impares são {sorted(impares)}')
