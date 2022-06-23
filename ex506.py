print('ANALISAR PESO E ALTURA')
nom1 = str(input('Digite o nome da primeira pessoa: ')).strip().upper()
pes1 = float(input('Digite o peso da primeira pessoa (kg): '))
alt1 = float(input('Digite a altura da primeira pessoa (m): '))
nom2 = str(input('Digite o nome da segunda pessoa: ')).strip().upper()
pes2 = float(input('Digite o peso da segunda pessoa (kg): '))
alt2 = float(input('Digite a altura da segunda pessoa (m): '))
if pes1 > pes2:
    print('A pessoa mais pesada é {} com {} kg'.format(nom1,pes1))
if pes2 > pes1:
    print('A pessoa mais pesada é {} com {} kg'.format(nom2, pes2))
if alt1 > alt2:
    print('A pessoa mais alta é {} com {:.2f} m'.format(nom1, alt1))
if alt2 > alt1:
    print('A pessoa mais alta é {} com {:.2f} m'.format(nom2, alt2))


#Crie um algoritmo que peça o nome, a altura e o peso de duas
#pessoas e apresente o nome da mais pesada e o nome da mais alta.