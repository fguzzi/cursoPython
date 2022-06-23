print('ANALISE DE NÚMEROS POSITIVOS E NEGATIVOS')
somapositivo = 0
totnegativo = 0
qtde = int(input('Quantos números você vai digitar? '))
for c in range(1,qtde + 1):
    num = int(input('Digite o {}º número: '.format(c)))
    if num >= 0:
        somapositivo = somapositivo + num
    if num < 0:
        totnegativo = totnegativo + num
print('A soma dos números positivos é {}'.format(somapositivo))
print('O total de números negativos é {}'.format(totnegativo))


#leia 20 números e imprima a soma
#dos positivos e o total de números negativos