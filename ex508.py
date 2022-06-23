print('NÚMEROS DE 5 A 500 MULTIPLOS DE 7 E NÃO MULTIPLOS DE 5')
tot = 0
for c in range(5, 501):
    if c % 7 == 0 and c % 5 != 0:
        tot += 1
        print(c, end=' ')






#todos os números entre 5 e 100 que são divisíveis por 7,
#mas não são múltiplos de 5. Os números obtidos devem ser impressos em sequência.