print('CONVERSOR DE MEDIDAS')
while True:
    print(''' OPÇÕES DISPONÍVEIS:
        [ 1 ] m/s para km/h
        [ 2 ] knots para km/h
        [ 3 ] jardas para m
        [ 4 ] pol para m
        [ 5 ] milhas para km''')
    op = int(input('Escolha a opção: '))
    if op == 1:
        vel = float(input('Digite a velocidade em m/s: '))
        km = (vel / 1000) * 3600
        print(f' A velocidade é {km:.1f} km/h')
    if op == 2:
        vel = float(input('Digite a velocidade em nós: '))
        km = vel * 1.8
        print(f' A velocidade é {km:.1f} km/h')
    if op == 3:
        jd = float(input('Digite a distância em jardas: '))
        m = jd * 0.9144
        print(f' A distância é {m:.1f} metros')
    if op == 4:
        pol = float(input('Digite a distância em polegadas: '))
        m = pol * 0.0254
        print(f' A distância é {m:.1f} metros')
    if op == 5:
        dist = float(input('Digite a distânia em milhas: '))
        km = dist * 1.852
        print(f' A distância é {km:.1f} kilometros')
    else:
        print('Opção inválida.')
    esc = str(input('Deseja continuar? [ S/N ]: ')).strip().upper()
    if esc== 'N':
        break
print('Encerrado')
