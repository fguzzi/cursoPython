from time import sleep
from random import randint
def sorteia(lista):
    print('Sorteando 5 valores da lista: ',end=' ')
    for i in range(0,5):
        n = randint(1,10)
        lista.append(n)
        sleep(1)
        print(n, end=' ')
    print(' -  PRONTO.')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma = soma + valor
    print(f' A soma dos numeros pares de {lista} é {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)














