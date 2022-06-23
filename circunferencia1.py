import math
print('*'*5, 'PROPRIEDADES DA CIRCUNFERENCIA','*'*5)
raio = float(input('Digite o raio da circunferência: '))
area = (math.pow(raio,2) * math.pi)
comprimento = (2 * (math.pi )* raio)
diâmetro = raio * 2
print('A área da cicunferência é: {:.2f}'.format(area))
print('O comprimento da circunferência é: {:.2f}'.format(comprimento))
print('O diâmetro da circunferência é {}'.format(diâmetro))
