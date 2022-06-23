# estrutura condicional aninhada

nome = str(input('Digite seu nome: '))
if nome == 'Fábio':
    print('Que nome lindo !!!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil !!!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Que lindo nome feminino !!!')
else:
    print('Seu nome é muito comum !!!')
print('Tenha um bom dia, {}'.format(nome))
