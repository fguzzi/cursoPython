print('INDEXANDO LISTA SEM COMANDO SORTED')
val = list()
i = 0
a = int(input('Digite o primeiro nº: '))
val.append(a)
print('Valor adicionado no final da lista')
b = int(input('Digite o segundo nº: '))
if b < a:
    val.insert(0, b)
    print('Valor adicionado na posição 0 da lista')
if b > a:
    val.insert(2, b)
    print('Valor adicionado no final da lista')
if b == a:
    val.insert(1, b)
    print('Valor adicionado no final da lista')
c = int(input('Digite o terceiro nº: '))
if c > val[1]:
    val.insert(2, c)
    print('Valor adicionado no final da lista')
if c < val[0]:
    val.insert(0, c)
    print('Valor adicionado na posição 0 da lista')
if c > val[0] and c < val[1]:
    val.insert(1, c)
    print('Valor adicionado na posição 1 da lista')
d = int(input('Digite o quarto nº: '))
if d > val[2]:
    val.insert(3, d)
    print('Valor adicionado no final da lista')
if d < val[0]:
    val.insert(0, d)
    print('Valor adicionado na posição 0 da lista')
if d > val[0] and d < val[1]:
    val.insert(1, d)
    print('Valor adicionado na posição 1 da lista')
if d > val[1] and d < val[2]:
    val.insert(2, d)
    print('Valor adicionado na posição 2 da lista')
e = int(input('Digite o quinto nº: '))
if e > val[3]:
    val.insert(4, e)
    print('Valor adicionado no final da lista')
if e < val[0]:
    val.insert(0, e)
    print('Valor adicionado na posição 0 da lista')
if e > val[0] and e < val[1]:
    val.insert(1, e)
    print('Valor adicionado na posição 1 da lista')
if e > val[1] and e < val[2]:
    val.insert(2, e)
    print('Valor adicionado na posição 2 da lista')
if e > val[2] and e < val[3]:
    val.insert(3, e)
    print('Valor adicionado na posição 3 da lista')
print(f'Números digitados em ordem alfabética são {val}')

