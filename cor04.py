# criando uma variável cores (dicionário)
nome = 'Fábio'
cores = {'limpa' : '\033[m',
               ' azul' : '\033[34m',
               'amarelo': '\033[33m',
               'pretoebranco' : '\033[7;30m'}
print('Olá, prazer em conhecê-lo, {} {} {}'.format(cores ['pretoebranco'], nome, cores ['limpa']))

