print('TIMES DO BRASILEIRÃO 2017')
times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo', 'Vasco',
         'Chapecoense', 'Atletico MG', 'Botafogo', 'Atletico PR', 'Bahia', 'Sao Paulo',
         'Fluminense', 'Sport', 'Vitoria', 'Coritiba', 'Avai', 'Atletico GO', 'Goias')
print('=' *30)
print('Os 20 times do Brasileirão 2017 são {}: '.format(times))
print('=' *30)
print('Os cinco primeiro times são: {}'.format(times[0:5]))
print('=' *30)
print('Os últimos quatro colocados são: {}'.format(times[-4:]))
print('=' *30)
print('Os times em ordem alfabética são: {}. '.format(sorted(times)))
print('=' *30)
for cont in range(0, len(times)):
    if times[cont] == 'Chapecoense':
        print('O time {} está em {}º lugar'.format(times[cont], cont+1))
print('=' *30)
