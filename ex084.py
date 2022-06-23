print('VERIFICANDO PESOS')
princ = []
temp = []
mai = men = 0
while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(float(input('Digite o peso em Kg: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    esc = str(input('Deseja continuar? [ S/N ]: '))
    if esc in 'Nn':
       break
print('=-'* 30)
print(f' Você cadastrou {len(princ)} pessoas.')
print(f'O maior peso é de {mai} Kg. Peso de', end = ' ')
for p in princ:
    if p[1] == mai:
        print(f' [{p[0]}]', end= ' ')
print(f' O menor peso é de {men} Kg. Peso de', end=' ')
for p in princ:
    if p[1] == men:
        print(f' [{p[0]}]',end=' ')
