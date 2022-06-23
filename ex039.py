from datetime import date
print('\033[1:33mVerificação de Alistamento Militar\033[m')
nasc = int(input('Digite o ano de seu nascimento: '))
atual = date.today().year
idade = atual - nasc
if idade == 18:
    print('Você tem que se alistar imediatamente.')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('FALTAM {} anos para você se alistar.'.format(saldo))
    print('Seu ano de alistamento será {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você está {} anos atrasado em seu alistamento.'.format(saldo))
    print('Seu ano de alistamento foi {}'.format(ano))
