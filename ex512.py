print(f' {"SORTEIO DA CARTA DO BARALHO":^30}')
print('=' *29)
import random
from random import choice
cartas = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K')
naipes = ('Copas', 'Espadas', 'Ouro', 'Paus')
while True:
    x = random.choice(cartas)
    y = random.choice(naipes)
    print(f' A carta sorteada foi {x} de {y}')
    esc = str(input('Deseja sortear outra carta? [ S/N ] ')).strip().upper()
    if esc == 'N':
        break
print('Programa encerrado.')
