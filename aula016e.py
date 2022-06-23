print('JUNTANDO TUPLAS')
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(a)
print(b)
print(a + b)
print(b + a)
print(len(c))
print(c.count(5))    # quantas vezes o 5 aparece em c
print(c)
print(c.index(8))  # em que posição está o 8
print(c.index(2))  # em que posição está o 2 - nesse caso é mostrada primeira ocorrência do número, já que ele aparece duas vezes
print(c.index(5, 1))  # em que posição está o 5 a partir da posição 1

# Importante: a + b não é igual a b + a


