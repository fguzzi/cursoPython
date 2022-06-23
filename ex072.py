print('PROCURAR NÚMERO EM UMA TUPLA')
numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
i = ''
while True:
    op = int(input('Digite um número entre 0 e 20: '))
    if 0 <= op <= 20:
        break
    print('Tente novamente.', end=' ')
print('Você digitou o número {}.'.format(numeros[op]))
