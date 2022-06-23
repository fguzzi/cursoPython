print('LISTA DE PESSOAS')
pessoa = dict()
galera = list()
soma = media = 0
idade = list()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [ M/F ]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO ! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [ S/N ] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO ! Digite apenas S ou N')
    if resp == 'N':
        break
print('='*30)
print(f' A) Ao todo foram cadastradas {len(galera)} pessoas.')
media = soma / len(galera)
print(f' B) A média de idade da lista é {media:5.2f}.')
print(' C) As mulheres cadastradas foram', end=' ')
for p in galera:
    if p['sexo'] == 'F':
        print(f' [{p["nome"]}]', end=' ')
print()
print(' D) As pessoas com idade acima da foram',end=' ')
for p in galera:
    if p['idade'] >= media:
        print(f' [{p["nome"]} com {p["idade"]} anos]',end=' ')
print()
print('======ENCERRADO======')
