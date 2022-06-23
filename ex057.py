sexo = str(input('Digite seu sexo [ M / F ]: ')).strip().upper()[0]
while sexo not in 'MmFm':
    sexo = str(input('Dados inválidos. Informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
