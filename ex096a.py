print('CONTROLE DE TERRENOS')
print('-'*30)
def area(l, c):
    a = c * l
    print(f' A área de um terreno de {c} m x {l} m = {a:.1f} m². ')


print('CONTROLE DE TERRENOS')
print('-'*30)
c = float(input('Comprimento: '))
l = float(input('Largura: '))
area(l, c)
