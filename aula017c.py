#ligação entre listas
a = [4, 6, 7, 10]
b = a
print(f' lista{a}')
print(f' lista{b}')

#alterando um elemento alteram-se as duas listas
a[2] = 99
print(f' lista{a}')
print(f' lista{b}')

#cópia de uma lista
x = [5, 78, 200, 1011]
y = x[:]
print(f' lista{x}')
print(f' lista{y}')

#alterando um elemento teremos a modificação somente na lista que teve o elemento alterado
x[2] = 99
print(f' lista{x}')
print(f' lista{y}')





