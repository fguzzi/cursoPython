print('JOGO DE PAR OU IMPAR')
from random import randint
cont = 0
esc = ''
while True:
    jog = int(input('Diga um valor: '))
    comp = randint(0, 10)
    s = jog + comp
    esc = str(input('Par ou Impar ? [ P / I ] ')).strip().upper()
    if esc == 'P':
        if s % 2 == 0:
            print('Computador escolheu {} e você {}, total de {}. DEU PAR !'.format(comp, jog, s))
            print('Você venceu !!')
            cont = cont +1
        if s % 2 == 1:
            print('Computador escolheu {} e você {}, total de {}. DEU IMPAR !'.format(comp, jog, s))
            print('Você perdeu !!')
            break
    if esc == 'I':
        if s % 2 == 0:
            print('Computador escolheu {} e você {}, total de {}. DEU PAR !'.format(comp, jog,s))
            print('Você perdeu !!')
            break
        if s % 2 == 1:
            print('O computador escolheu {} e você {}, total de {}. DEU IMPAR !'.format(comp,jog,s))
            print(('Você venceu !'))
            cont = cont + 1
print('GAME OVER ! Você venceu {} vezes'.format(cont))
