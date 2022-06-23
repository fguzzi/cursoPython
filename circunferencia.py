print('CIRCUNFERÊNCIA')
from math import pi
while True:
    print(''' O que deseja calcular? 
               [ 1 ] Diâmetro da Circunferência
               [ 2 ] Area da Circunferência
               [ 3 ] Perímetro da Circunferência''')
    op = int(input('Digite sua opção: '))
    if op == 1:
        r = float(input('Digite o valor do raio: '))
        d = r * 2
        print(f' O valor do diâmetro = {d:.1f}')
    elif op == 2:
        r = float(input('Digite o valor do raio: '))
        a = pi * pow(r, 2)
        print(f' O valor da área é {a:.1f}')
    elif op == 3:
        r = float(input('Digite o valor do raio: '))
        p = 2 * (pi * r)
        print(f' O valor do perímetro é {p:.1f}')
    else:
        print('Opção inexistente. Tente novamente.')
    esc = str(input('Deseja continuar? [ S/N ]: ')).strip().upper()[0]
    if esc == 'N':
        break
print('Encerrado.')