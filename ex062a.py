print('GERADOR DE PA')
pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
termo = pri
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -- '.format(termo), end=' ')
        termo = termo + raz
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos números você que digitar a mais a mais? '))
print('Prograssão finalizada com {} termos mostrados'.format(total))
