print('*' * 60)
print("Equação do segundo grau, modelo ax² + bx  +  c =  0")
from math import pow, sqrt
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
d = ((pow(b,2)) - (4 * a * c))
x1 = ((-b) + (sqrt(d))) / (2 * a)
x2 = ((-b) - (sqrt(d))) / (2 * a)
print('As raízes dessa equação são: x1 = {} e x2 = {}'.format(x1, x2))
print('*' * 60)






