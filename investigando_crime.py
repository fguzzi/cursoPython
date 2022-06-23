print('<INVESTIGANDO UM CRIME>')
print('RESPONDA AS PERGUNTAS ABAIXO:')
sim = 0
p1 = str(input('Você telefonou para a vítima? [S/N] ')).strip().upper()
if p1 == 'S':
    sim = sim + 1
p2 = str(input('Mora perto da vítima? [S/N] ')).strip().upper()
if p2 == 'S':
    sim = sim + 1
p3 = str(input('Devia para a vítima? [S/N] ')).strip().upper()
if p3 == 'S':
    sim = sim + 1
p4 = str(input('Já trabalhou com a vítima? [S/N] ')).strip().upper()
if p4 == 'S':
    sim = sim + 1
p5 = str(input('Esteve no local do crime? [S/N] ')).strip().upper()
if p5 == 'S':
    sim = sim + 1
if sim == 2:
    print('Você é SUSPEITO do crime !!!')
elif sim == 3 or sim == 4:
    print('Você é CÚMPLICE do crime !!!')
elif sim == 5:
    print('Você é O CRIMINOSO !!!')
else:
    print('Você é INOCENTE !!!')

# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação
# sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada
# como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".#
