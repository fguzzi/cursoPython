print('IDENTIFICANDO PESSOAS MENORES E MAIORES DE IDADE')
from datetime import date
totmaior = 0
totmenor = 0
for pess in range(1,8):
     nasc = int(input('Em que ano nasceu a {}ª pessoa? '.format(pess)))
     atual = date.today().year
     idade = atual - nasc
     if idade >= 21:
          totmaior += 1
     else:
          totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade e {} menores.'.format(totmaior, totmenor))


