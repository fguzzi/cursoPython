print('MOSTRAR OS 10 PRIMEIROS TERMOS DE UMA PA')
pri = int(input('Informe o primeiro termo: '))
raz = int(input('Informe a razão: '))
pa = pri - raz
i = 0
while i < 10:
    pa = pa + raz
    i = i + 1
    print(pa, end=' ')
menu = str(input('Você deseja digitar mais números? [ S/N] ')).strip().upper()
while menu == 'S':
    pri = int(input('Informe o primeiro termo: '))
    raz = int(input('Informe a razão: '))
    pa = pri - raz
    i = 0
    while i < 10:
        pa = pa + raz
        i = i + 1
        print(pa, end=' ')
    menu = str(input('Você deseja digitar mais números? [ S/N] ')).strip().upper()
print('FIM !!')
