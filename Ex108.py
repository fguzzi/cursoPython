import moedadois

p = float(input('Digite o preço em R$ '))
print(f' A metade de {moedadois.moedadois(p)} é {moedadois.moedadois(moedadois.metade(p))}')
print(f' O dobro de {moedadois.moedadois(p)} é {moedadois.moedadois(moedadois.dobro(p))}')
print(f' Aumentando 10% em {moedadois.moedadois(p)} o preço é {moedadois.moedadois(moedadois.aumentar(p,10))}')
print(f' Diminuindo 10% em {moedadois.moedadois(p)} o preço é {moedadois.moedadois(moedadois.diminuir(p, 10))}')
