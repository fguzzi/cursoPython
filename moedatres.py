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


def moedatres(preco=0, moedadois='R$'):
    return f' {moedadois}{preco:>.2f}'.replace("." , ",")

# usado pelo exercicio 109
