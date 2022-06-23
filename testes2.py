from random import randint
n = ['pelé', 'zico', 'rivelino']
v = [2, 6, 6]
m = 0
for c in v:
    if c > m:
        m = c
    i = v.index(m)
    q = v.count(m)
if q > 1:
    print('Empatou')
else:
    print(f' O vencedor foi {n[i]} com {m} pontos')



