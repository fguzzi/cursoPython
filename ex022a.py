nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome:')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Quantidade de letras de seu nome = {}'.format((len(nome)) - (nome.count(' '))))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))


