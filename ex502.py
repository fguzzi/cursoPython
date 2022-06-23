print('SOMA DE NÚMEROS PARES E IMPARES DE UM INTERVALO DE 10 NÚMEROS')
somapar = 0
somaimpar =0
for c in range(1,11):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        somapar += num
    else:
        somaimpar += num
print('A soma dos números pares é {} e dos impares é {}'.format(somapar,somaimpar))


 #leia 10 números inteiros e imprima
#quantos são pares e quantos são ímpares.