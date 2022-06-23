print('SOMA DE FRAÇOES')
soma = 0
while True:
    print('Soma de Frações')
    n = int(input('Digite o numerador: '))
    d = int(input('Digite o denominador: '))
    print('Fração solicitada: {} / {}'.format(n, d))
    if d > 0:
        x = n / d
        soma = soma + x
        esc = str(input('Deseja inserir outra fração? [ S/N ] ')).strip().upper()[0]
        if esc == 'N':
            break
    if d == 0:
        print('Não existe divisão por 0')
        break
if soma > 0:
    print('A soma das frações é {}'.format(soma))

