print('IDENTIFICANDO PESSOAS MENORES DE 21 ANOS')
from datetime import date
for c in range(1,8):
    an = int(input('Em que ano nasceu a {}ª pessoa: '.format(c)))
    if an > 2022:
        print('Opção inválida !! Tente novamente !')
    elif (an + 21) > date.today().year:
        print('\033[33mEssa pessoa nasceu em {} e não atingiu a maioridade\033[m'.format(an))
    else:
        print('\033[31mEssa pessoa nasceu em {} e é de maioridade\033[m'.format(an))
