print('EXTRAINDO DADOS DA LISTA')
l = list()
while True:
    l.append(int(input('Digite um nº: ')))
    esc = str(input('Deseja continuar digitando? [ S/N ]: '))
    if esc in 'Nn':
        break
print(f' Foram digitados {len(l)} números.')
l.sort(reverse=True)
print(f' Os valores em ordem decrescente são {l}')
if 5 in l:
    print(f' O valor 5 está presente na lista')
else:
    print(f' O valor 5 não foi encontrado na lista')
