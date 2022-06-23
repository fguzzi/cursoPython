# Dicionário dentro de uma lista

brasil = []
estado1 = {'UF' : 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)

print(brasil[0]['UF'])
print(brasil[1]['UF'])

print(brasil[1]['Sigla'])



