print('OPERAÇÕES ENTRE DOIS NÚMEROS INTEIROS')
from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
menu = 0
print('''O que você deseja realizar:
      [ 1 ] - Somar
      [ 2 ] - Multiplicar
      [ 3 ] - Maior
      [ 4 ] - Novos números
      [ 5 ] - Sair do programa''')
while menu != 5:
    menu = int(input('Qual a sua opção: '))
    if menu == 1:
        soma = num1 + num2
        print('A soma dos números é igual a {}'.format(soma))
        print('''O que você deseja realizar:
              [ 1 ] - Somar
              [ 2 ] - Multiplicar
              [ 3 ] - Maior
              [ 4 ] - Novos números
              [ 5 ] - Sair do programa''')
    elif menu == 2:
        mult = num1 * num2
        print('A multiplicação dos produto dos números é igual a {}'.format(mult))
        print('''O que você deseja realizar:
              [ 1 ] - Somar
              [ 2 ] - Multiplicar
              [ 3 ] - Maior
              [ 4 ] - Novos números
              [ 5 ] - Sair do programa''')
    elif menu == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
            print('Entre {} e {}, o número {} é o maior número'.format(num1, num2, maior))
            print('''O que você deseja realizar:
                  [ 1 ] - Somar
                  [ 2 ] - Multiplicar
                  [ 3 ] - Maior
                  [ 4 ] - Novos números
                  [ 5 ] - Sair do programa''')
        if num1 == num2:
            print('Os números são iguais')
            print('''O que você deseja realizar:
                  [ 1 ] - Somar
                  [ 2 ] - Multiplicar
                  [ 3 ] - Maior
                  [ 4 ] - Novos números
                  [ 5 ] - Sair do programa''')
    elif menu == 4:
        print('Digite os números novamente.')
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        print('''O que você deseja realizar:
                          [ 1 ] - Somar
                          [ 2 ] - Multiplicar
                          [ 3 ] - Maior
                          [ 4 ] - Novos números
                          [ 5 ] - Sair do programa''')
if menu == 5:
        print('Finalizando...')
        sleep(1)
        print('O programa foi finalizado')
else:
        print('Opção inválida')


