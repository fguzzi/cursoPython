from random import randint
z = 0
x = 5
n = (randint(z,x), randint(z,x), randint(z,x), randint(z,x), randint(z,x))
id = (sorted(n))
print('Os números sortados foram: {}'.format(n))
print('O nº maior é {} e o menor é {}'.format(id[x-1], id[z]))
