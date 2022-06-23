print('SOMA DE NÚMEROS')
s = cont = 0
while True:
    n = int(input('Digite um nº (999 para encerrar): '))
    if n == 999:
        break
    cont += 1
    s += n
print('A soma dos {} números é {}'.format(cont, s))
