print('ANALISE DE UMA TUPLA')
num = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print('Você digitou os valores {}.'.format(num))
print('O valor 9 apareceu {} vezes.'.format(num.count(9)))
if 3 in num:
    print('O valor 3 apareceu pela primeira vez na {}ª posicão.'.format(num.index(3) + 1))
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
