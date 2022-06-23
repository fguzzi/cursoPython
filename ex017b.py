from math import hypot

co = float(input('Digite a medida do cateto oposto: '))
ca = float(input('Digite a medida do cateto adjacente: '))
hip = hypot(co,ca)
print('Cateto oposto é {} e cateto adjacente  é {}, sendo assim, a hipotenusa é {:.2f}'.format(co, ca, hip))
