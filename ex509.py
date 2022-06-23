print('SOMA DE TODOS NÚMEROS ANTERIORES')
somanum = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    somanum = somanum + c
print('A soma do número {} com seus anteriores até 1 é {}'.format(num,somanum))


#Faça um programa que
#receba um número digitado pelo usuário e calcule a soma de todos os números de 1 até ao número digitado.