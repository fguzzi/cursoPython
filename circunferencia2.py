from math import pow, pi
print('*'*5, 'PROPRIEDADES DA CIRCUNFERENCIA','*'*5)
raio = float(input('Digite o raio da circunferência: '))
print('A área da cicunferência é: {:.2f}'.format(pow(raio,2)*pi))
print('O comprimento da circunferência é: {:.2f}'.format((pi*2)*raio))
print('O diâmetro da circunferência é: {:.1f}'.format(raio * 2))
