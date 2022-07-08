import moedatres

p = float(input('Digite o preço em R$ '))
print(f' A metade de {moedatres.moedatres(p)} é {moedatres.metade(p, True)}')
print(f' O dobro de {moedatres.moedatres(p)} é {moedatres.dobro(p, True)}')
print(f' Aumentando 10% em {moedatres.moedatres(p)} o preço é {moedatres.aumentar(p,10, True)}')
print(f' Diminuindo 10% em {moedatres.moedatres(p)} o preço é {moedatres.diminuir(p, 10, True)}')
