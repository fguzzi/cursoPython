print('DECOMPONDO UM NÚMERO')
num = int(input('Digite um número inteiro < 1000: '))
if num >= 1000:
    print('Opção inválida.')
else:
    centenas = num // 100
    dezenas = ((num % 100) // 10)
    unidades = num - ((centenas * 100) + (dezenas * 10))
    print('O número {} tem:'.format(num))
    print('{} centenas'.format(centenas))
    print('{} dezenas'.format(dezenas))
    print('{} unidades'.format(unidades))

#Faça um Programa que leia um número inteiro menor que 1000 e imprima
#a quantidade de centenas, dezenas e unidades do mesmo







