print('DISTÂNCIAS ENTRE NOTAS PARTINDO DA TÔNICA')
notas = ['Primeira', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sétima', 'Oitava']
dist = [1,2,2.5, 3.5, 4.5, 5.5, 6]
while True:
    print('''Qual a posição da 2ª nota na escala?
               [ 1 ] - Primeira(Tônica)
               [ 2 ] - Segunda
               [ 3 ] - Teça
               [ 4 ] - Quarta
               [ 5 ] - Quinta
               [ 6 ] - Sexta
               [ 7 ] - Sétima
               [ 8 ] - Oitava''')
    esc1 = int(input('Digite: '))
    print(f' Você escolheu {notas[esc1-1]}')
    if esc1 == 1:
        print(f' Não há distância.')
    else:
        if esc1 == 2:
            print(f' A distância é de {dist[0]} tons')
        if esc1 == 3:
            print(f' A distância é de {dist[1]} tons')
        if esc1 == 4:
            print(f' A distância é de {dist[2]} tons')
        if esc1 == 5:
            print(f' A distância é de {dist[3]} tons')
        if esc1 == 6:
            print(f' A distância é de {dist[4]} tons')
        if esc1 == 7:
            print(f' A distância é de {dist[5]} tons')
        if esc1 == 8:
            print(f' A distância é de {dist[6]} tons')
    esc2 = str(input('Deseja continuar? [ S/N ]: ')).strip().upper()[0]
    if esc2 == 'N':
        break
print('Programa encerrado.')
