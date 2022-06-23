print('SOMA DOS NÚMEROS IMPARES MULTIPLOS DE 3 DE 0 A 500')
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores = {}'.format(cont,soma))





