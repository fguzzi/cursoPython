print('ANALISE DE SEQUÊNCIA DE NUMEROS')
n = soma = cont = 0
n = int(input('Digite um número qualquer ou 999 para encerrar o programa: '))
while n != 999:
        soma += n
        cont = cont + 1
        n = int(input('Digite um número qualquer ou 999 para encerrar o programa: '))
print('A soma dos {} números digitados é {}'.format(cont, soma))
