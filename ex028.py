from random import randint
from time import sleep
print('-=-' *20)
print('Vou pensar em um número de 0 a 5. Tente advinhar...')
print('-=-' *20)
num = randint(0,5)      # Faz o computador 'pensar' (sortear)
pal = int(input('Em que número eu pensei??? '))
print('PROCESSANDO...')
sleep(2)
if num == pal:
    print('Parabéns, você acertou !')
else:
    print('Ganhei !! Pensei no número {} e não no {} !!'.format(num,pal))

