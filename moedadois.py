def dobro(preco=0):
    res = preco * 2
    return res


def metade(preco=0):
    res = preco / 2
    return res


def diminuir(preco=0, taxa=0):
    res = preco - (preco * (taxa / 100))
    return res


def aumentar(preco=0, taxa=0):
    res = preco + (preco * (taxa / 100))
    return res


def moedadois(preco=0, moedadois='R$'):
    return f' {moedadois}{preco:>.2f}'.replace("." , ",")

# usado pelo exercicio 108
