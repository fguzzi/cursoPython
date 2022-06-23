print('VAMOS JOGAR DADOS !!!')
print('=' * 20)
from random import randint
from time import sleep
n = []
v = []
m = 0
while True:
    n.clear()
    v.clear()
    qt = int(input('Quantas pessoas irão jogar? '))
    for c in range(0, qt):
        nome = str(input(f' Nome do {c +1}º jogador: ')).strip().upper()
        valor = randint(1, 6)
        n.insert(0, nome)
        v.insert(0, valor)
        print('Jogando o dado...')
        sleep(1.5)
        print(f' {nome} tirou {valor}')
        print('-'*30)
    for c in v:
        if c > m:
            m = c
    i = v.index(m)
    q = v.count(m)
    if q > 1:
        print('EMPATOU !!!!')
    else:
        print(f' O vencedor foi {n[i]} com {m} pontos')
    op = str(input('Quer jogar novamente? [ S/N ]' )).strip().upper()
    if op == 'N':
        print('ENCERRADO.')
        break



