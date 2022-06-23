from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print(''' \033[1;35;4mSUAS OPÇÕES:\033[m
[ 0 ] - \033[31mPEDRA\033[m
[ 1 ] - \033[33mPAPEL\033[m
[ 2 ] - \033[34mTESOURA\033[m''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' *11)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' *11)
if jogador == 0:
    if computador == 0:
        print('EMPATOU !')
    elif computador == 1:
        print('COMPUTADOR VENCE !')
    elif computador == 2:
        print('JOGADOR VENCE !')
elif jogador == 1:
    if computador == 0:
        print('CJOGADOR VENCE !')
    elif computador == 1:
        print('EMPATOU !')
    elif computador == 2:
        print('COMPUTADOR VENCE !')
elif jogador == 2:
    if jcomputador == 0:
       print('COMPUTADOR VENCE !')
    elif computador == 1:
       print('JOGADOR VENCE !')
    elif computador == 2:
       print('EMPATOU')
else:
        print('JOGADA INVÁLIDA !')
