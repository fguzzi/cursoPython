from random import choice
print('JOKENPO')
pc = choice(['Pedra','Tesoura', 'Papel'])
jog = str(input('Escolha entre: Pedra, Tesoura e Papel: '))
if pc == jog:
    print('Você escolheu {} e eu {}. O jogo empatou !!!'.format(jog,pc))
elif pc == 'Pedra' and jog == 'Tesoura':
    print('Você escolheu {} e eu {}. Eu ganhei !!!!'.format(jog,pc))
elif pc == 'Tesoura' and jog == 'Pedra':
    print('Você escolher {} e eu {}. Você ganhou.'.format(jog,pc))
elif pc == 'Tesoura' and jog == 'Papel':
    print('Você escolheu {} e eu {}. Eu ganhei.'.format(jog,pc))
elif pc == 'Papel' and jog == 'Tesoura':
    print('Você escolheu {} e eu {}. Você ganhou.'.format(jog,pc))
elif pc == 'Papel' and jog == 'Pedra':
    print('Você escolheu {} e eu {}. Eu ganhei.'.format(jog,pc))
elif pc == 'Pedra' and jog == 'Papel':
    print('Você escolheu {} e eu {}. Você ganhou.'.format(jog,pc))
else:
    print('Você escolheu opção inexistente')


