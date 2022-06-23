pessoas = {'nome': 'Fábio', 'sexo': 'Masculino', 'idade': '58'}
print(pessoas)

print(pessoas['nome'])

print(f' O {pessoas["nome"]} tem {pessoas["idade"]} anos')

print(pessoas.keys())

print(pessoas.values())

print(pessoas.items())

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for k, v in pessoas.items():
    print(f' {k} = {v} ')

del pessoas[ 'sexo']
print(pessoas)

pessoas['nome'] = 'Henrique'
print(pessoas)

pessoas['peso'] = 97.9
print(pessoas)





