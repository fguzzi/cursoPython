from math import sin, cos, tan, radians
ang = float(input('Digite um ângulo, em graus: '))
seno = (sin(radians(ang)))
print('O seno de {}° é {:.2f} '.format(ang,seno))
cosseno = (cos(radians(ang)))
print('O cosseno de {}° é {:.2f} '.format(ang,cosseno))
tangente = tan(radians(ang))
print('A tangente de {}° é {:.2f} '.format(ang,tangente))
