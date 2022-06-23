print('**********CONTADOR*********')
from time import sleep
def contador(a, b, c):
    for i in range(a, b, c):
        sleep(1)
        print(i, end=' ')
    print(' --FIM--')


print('-'*40)
print('Contagem 1 a 10 de 1 em 1')
contador(1, 11, 1)
print()
print('-'*40)
print('Contagem de 10 a 0 de 2 em 2')
contador(10, 0, -2)
print()
print('-'*40)
print('Agora é sua vez de personalizar a contagem')
while True:
    a = int(input('Início: '))
    b = int(input('Fim: '))
    c = int(input('Passo: '))
    if c == 0:
        c = 1
    if a > b:
        c = - c
        print(f' Contagem de {a} até {b} de {- c} em {- c}')
    else: print(f' Contagem de {a} até {b} de {c} em {c}')
    if a > b:
        contador(a, b - 1, c)
    else:
        contador(a, b + 1, c)
    print()
    op = str(input('Deseja continuar? [ S/N ] ')).strip().lower()
    if op == 'n':
        break
print('ENCERRADO')
