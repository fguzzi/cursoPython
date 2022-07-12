def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moedatres(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moedatres(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * (taxa / 100))
    return res if not formato else moedatres(res)


def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * (taxa / 100))
    return res if not formato else moedatres(res)


def moedatres(preco=0, moedadois='R$ '):
    return f' {moedadois}{preco:>.2f}'.replace("." , ",")


def resumo(preco=0, taxaa=10, taxar=5):
    print('-' *50)
    print('RESUMO DO VALOR'.center(20))
    print('-' *50)
    print(f' Preço Analisado é \t\t{moedatres(preco)}')
    print('-' * 50)
    print(f' O dobro do preço é \t{dobro(preco, True)}')
    print('-' * 50)
    print(f' A metade do preço é \t{metade(preco, True)}')
    print('-' * 50)
    print(f' {taxar} % de redução: \t\t{diminuir(preco, taxar, True)}')
    print('-' * 50)
    print(f' {taxaa} % de aumento: \t\t{aumentar(preco, taxaa, True)}')
    print('-' * 50)
