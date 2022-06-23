import math
ang = float(input('Digite um ângulo, em graus: '))
seno = (math.sin(math.radians(ang)))
print('O seno de {}° é {:.2f} '.format(ang,seno))
cosseno = (math.cos(math.radians(ang)))
print('O cosseno de {}° é {:.2f} '.format(ang,cosseno))
tangente = math.tan(math.radians(ang))
print('A tangente de {}° é {:.2f} '.format(ang,tangente))
