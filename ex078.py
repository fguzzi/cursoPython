print('VERIFICANDO NUMEROS MAIORES E MENORES NA LISTA')
num = []
mai = 0
men = 0
for cont in range(0, 5):
    num.append(int(input(f' Digite um número para a posição {cont}: ')))
    if cont == 0:
        mai = men = num[cont]
    else:
        if num[cont] > mai:
            mai = num[cont]
        if num[cont] < men:
            men = num[cont]
print('-='* 30)
print(f' Você digitou os valores {num}')
print(f' O maior valor é {mai} nas posições ', end=' ')
for i, v in enumerate(num):
    if v == mai:
        print(f' {i}...', end=' ')
print()
print(f' O menor valor é {men} nas posições ', end=' ')
for i, v in enumerate(num):
    if v == men:
        print(f' {i}...', end=' ')
print()

