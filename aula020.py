# função para somar dois parâmetros
def soma(a, b):
    print(f' A = {a} e B = {b}')
    s = a + b
    print(f' A soma A + B = {s}')


soma (17, 1000)
soma(b=17, a=1000)

# empacotamento de parâmetros com *
def contador(*num):
    for valor in num:
        print(f' {valor}  ', end=' ')
    print('FIM')


contador(2, 1, 7)
contador(3, 2, 7, 90)

#variação do anterior
def contador(*num):
   tam = len(num)
   print(f' Recebi os valores {num} e são ao todo {tam}')


contador(2, 1, 7)
contador(3, 2, 7, 90)

# trabalhando com uma lista - dobrando seus valores

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [2, 3, 7, 12, 36, 122]
dobra(valores)
print(valores)
