h = float(input('Altura de sua  parede: '))
l = float(input('Largura de sua  parede: '))
area = h * l
tinta = (area / 2)
print(
    'Sua parede tem {:.2f} de altura por {:.2f} de largura e sua área é de {:.2f} metros quadrados'.format(h, l, area))
print('Necessário {:.1f}  l de tinta para pintar sua parede'.format(tinta))

#  cada litro de tinta pinta 2 metros quadrados
