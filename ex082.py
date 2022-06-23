print('TRES LISTAS')
lcomp = list()
lpar = list()
limpar = list()
while True:
    lcomp.append(int(input('Digite um número: ')))
    esc = str(input('Deseja continuar digitando? [ S/N ]: ')).strip().upper()[0]
    if esc == 'N':
        break
for i in lcomp:
    if i % 2 == 0:
        lpar.append(i)
    else:
        limpar.append(i)
print(f' A lista completa é {lcomp}')
print(f' A lista de números pares é {lpar}')
print(f' A lsita de número ímpares é {limpar}')
