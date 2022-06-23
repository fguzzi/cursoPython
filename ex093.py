print('ANALISE JOGADOR DE FUTEBOL')
nome = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas jogou? '))
gols = []
for i in range(1, partidas + 1):
    g = int(input(f'Gols na {i}ª partida: '))
    gols.append(g)
soma = 0
for c in range(0, len(gols)):
    soma = soma + gols[c]
dados = {'Nome': nome, 'Gols': gols[:], 'Total': soma}
print(dados)
print('=='*30)
print(f' O campo nome tem o valor {nome}')
print(f' O campo gols tem o valor {gols}')
print(f' O campo total tem o valor {soma}')
print('=='*30)
print(f' O jogador {nome} jogou {partidas} partidas.')
for x in range(0, partidas):
    print(f' Na partida {x+1}, marcou {gols[x]} gol(s).')
