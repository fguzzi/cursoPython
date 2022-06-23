import math
co = float(input('Digite a medida do cateto oposto: '))
ca = float(input('Digite a medida do cateto adjacente: '))
hip = math.sqrt((math.pow(co,2)) + (math.pow(ca,2)))
print('Cateto oposto é {} e cateto adjacente  é {}, sendo assim, a hipotenusa é {:.2f}'.format(co, ca, hip))
