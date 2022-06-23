from random import randint
from time import sleep
pessoas = []
valores = []
while True:
    pessoas.clear()
    valores.clear()
    q = int(input('Qtos jogadores? : '))
    for cont in range(0, q):
        n = str(input(f' Nome do {cont + 1}º jogador: ')).strip().upper()
        v = randint(1, 6)
        print('Jogando o dado...')
        sleep(1)
        print(f' {n} tirou {v}.')
        pessoas.insert(0, n)
        valores.insert(0, v)
        i = valores.index(max(valores))
    print(f' O vencedor foi {pessoas[i]} com {max(valores)}')
    op = str(input('Deseja jogar novamente? [ S/N ]: ')).strip().upper()
    if op == 'N':
        print('ENCERRADO')
        break
