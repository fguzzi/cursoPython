print('ANALISANDO PALÍNDROMO')
frase = str(input('Digite uma frase: '))
fraseinv = frase [:: -1]
print('A frase digitada é \033[4;32m{}\033[m'.format(frase))
print('A mesma frase lida ao contrário é \033[4;32m{}\033[m'.format(fraseinv))
print('Portanto: ')
if frase == fraseinv:
    print('A frase é um palíndromo, pois lida ao contrário é identica ao normal'.format(frase))
else:
    print('A frase \033[4;32m{}\033[m não é um palíndromo, pois lida ao contrário está diferente do normal'.format(frase))
