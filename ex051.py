print('ANALISANDO UMA PA')
primeiro = int(input('Informe o primeiro termo: '))
razão = int(input('Informe a razão: '))
décimo = primeiro + (10 -1) * razão
for c in range(primeiro, décimo + razão, razão):
    print(' {} '.format(c), end=' - ')
print('ACABOU !!')


