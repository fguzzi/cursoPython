print('INDEXANDO LISTA SEM COMANDO SORTED')
list = []
for i in range (0, 5):
    n = int(input('Digite um número: '))
    if i == 0 or n > list[len(list) -1]:
        list.append(n)
        print('Valor inserido no final da lista')
    else:
        pos = 0
        while pos < len(list):
            if n <= list[pos]:
                list.insert(pos, n)
                print(f' Adicionado a posição {pos} da lista...')
                break
            pos += 1
print(f' Os valores digitados na ordem foram {list}')
