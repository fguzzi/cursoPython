print('INDEXANDO UMA LISTA')
num = list()
while True:
    x = (int(input('Digite um nº: ')))
    if x not in num:
        num.append(x)
        print('Valor adicionado com sucesso.')
    else:
        print('Número já existente. Não vou adicionar.')
    escolha = str(input('Deseja continuar? [ S/N ]: ')).strip().upper()[0]
    if escolha == 'N':
       print(f' Você digitou {sorted(num)}')
       break
