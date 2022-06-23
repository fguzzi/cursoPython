print('MOSTRANDO AS VOGAIS')
palavras = ('vagas', 'pedra', 'marceneiro', 'biblia', 'livro', 'caderno', 'araraquara',
         'fluminense', 'ferroviaria', 'guitarra')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
