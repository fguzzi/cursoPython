#criando uma lista
num = [3, 5, 9, 1]
print(num)

#modificando o item 2 da lista
num[2] = 7
print(num)

#inserindo mais um elemento
num.append(15)
print(num)

#colocando em ordem crescente a lista
num.sort()
print(num)

#colocando em ordem decrescente
num.sort(reverse=True)
print(num)

#contando elementos da lista
print(f'Essa lista tem {len(num)} elementos')

#inserindo na posição 2 o valor 0
num.insert(2, 0)
print(num)

#eliminando o último elemento
num.pop()
print(num)

#eliminando o elemento 2 que é 0
num.pop(2)
print(num)

#verificar se um elemento está na lista antes de remover
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número.')

#criar uma lista através de list e exibir valores
valores = list()
valores.append(5)
valores.append(56)
valores.append(199)
for v in valores:
    print(f'{v}...')

#criar uma lista através de list e exibir valores e índices
listagem = [-17, 89, -176]
for c, v in enumerate(listagem):
    print(f'Na posição {c}, temos o valor {v}')
print("Cheguei ao final da lista")












