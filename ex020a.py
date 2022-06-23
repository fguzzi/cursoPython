from random import shuffle
n1 = str(input('Aluno1: '))
n2 = str(input('Aluno2: '))
n3 = str(input('Aluno3: '))
n4 = str(input('Aluno4: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação dos trabalhos será:')
print(lista)
