print('ANALISE JOGADORES DE FUTEBOL')
jogador = dict()
gols = list()
time = list()
while True:
    jogador['nome'] = str(input('Qual o nome do jogador? '))
    jogador['partidas'] = int(input(f' Quantas partidas {jogador["nome"]} jogou? '))
    for cont in range(0, jogador['partidas']):
        gols.append(int(input(f' Quantos gols marcou na {cont + 1}ª partida? ')))
    jogador['gols'] = gols[:]
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()
    op = str(input('Deseja continuar? [ S/N ]: ')).strip().upper()[0]
    if op in 'Nn':
        break
print('=' * 30)
print('cod', end=' ')
for i in jogador.keys():
    print(f' {i:<15}', end= ' ')
print()
print('-' *40)
for k, v in enumerate(time):
    print(f' {k:>3}', end=' ')
    for d in v.values():
        print(f' {str(d):<15}', end=' ')
print()
print('-' *40)
while True:
    busca = int(input('Mostrar dados de qual jogador? [ 999 para parar ]: '))
    if busca == 999:
        print('ENCERRADO')
        break
    if busca >= len(time):
        print(f' NÃO EXISTE JOGADOR COM CÓDIGO {busca}')
    else:
        print(f' --LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} :')
        for i, g in enumerate(time[busca]['gols']):
            print(f'      No jogo {i + 1} fez {g} gols. ')
