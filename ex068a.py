print('JOGO DE PAR OU IMPAR')
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [ P / I ] ')).strip().upper()[0]
    print('Você jogou {} e o computador {}. Total de {}'.format(jogador, computador, total))
    print('Deu PAR ' if total % 2 == 0 else 'Deu IMPAR ')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce venceu !')
            v += 1
        else:
            print('Você perdeu !')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você venceu !')
            v += 1
        else:
            print('Você perdeu !')
            break
    print('Vamos jogar novamente...')
print('GAME OVER ! Você conseguiu {} vitórias'. format(v))
