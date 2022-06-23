from random import randint
from time import sleep
computador = randint(0,10)      # Faz o computador 'pensar' (sortear)
print('-=-' *20)
print('Olá ! Sou seu computador !!')
print('Vou pensar em um número de 0 a 5. Será que você advinha?')
print('-=-' *20)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite ??? '))
    palpite += 1
    print('PROCESSANDO...')
    sleep(1)
    if computador == jogador:
        acertou = True
    else:
        if computador > jogador:
            print('É mais... Tente outra vez.')
        elif computador < jogador:
            print('É menos... Tente outra vez.')
print('Parabéns, você acertou com {} tentativas !'.format(palpite))
