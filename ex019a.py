from random import choice
n1 = str(input('Aluno1: '))
n2 = str(input('Aluno2: '))
n3 = str(input('Aluno3: '))
n4 = str(input('Aluno4: '))
lista = [n1,n2,n3,n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'. format(escolhido))
