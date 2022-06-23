print('MOSTRAR O MAIOR E O MENOR NÚMERO EM UMA SEQUENCIA')
maior = 0
menor = 0
qtde = int(input('Quantos números terá sua sequência? '))
for c in range(1, qtde+1):
    num = int(input('Digite o {}º número: '.format(c)))
    if c == 1:
             maior = num
             menor = num
    else:
         if num > maior:
             maior = num
         if num < menor:
             menor = num
print('O maior número é {} e o menor é {}'.format(maior,menor))


# leia  números inteiros e imprima
#o maior e o menor número.