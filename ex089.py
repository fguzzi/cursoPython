print('LISTA DE NOTAS')
lcomp = list()
nome = list()
nota1 = list()
nota2 = list()
c = 0
while True:
    nome.append(str(input('Nome do aluno: ')))
    nota1.append(float(input('Nota 1: ')))
    nota2.append(float(input('Nota 2: ')))
    op = str(input('Deseja continuar? [ S/N ]: ')).strip().upper()
    if op == 'N':
        break
lcomp.append(nome)
lcomp.append(nota1)
lcomp.append(nota2)
print('Nº        NOME         MÉDIA')
for i in range(0, len(nome)):
    nome = lcomp[0][i]
    media = ((lcomp[1][i] + lcomp[2][i]) / 2)
    print(f' {i+1}         {nome}          {media}')
while True:
    esc = str(input('Deseja ver as notas de que aluno?: ')).strip()
    for x in range(0, len(lcomp[0])):
        if esc == lcomp[0][x]:
           print(f' As notas do aluno {lcomp[0][x]} são: {lcomp[1][x]} e {lcomp[2][x]}')
    pref = str(input('Deseja continuar? [ S/N ] ')).strip().upper()
    if pref == 'N':
        print('Programa encerrado.')
        break
