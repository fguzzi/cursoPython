print('ANALISE JOGADOR DE FUTEBOL')
jogador = dict()
gols = list()
jogador['nome'] = str(input('Qual o nome do jogador? '))
jogador['partidas'] = int(input(f' Quantas partidas {jogador["nome"]} jogou? '))
for cont in range(1, jogador['partidas'] +1):
    gols.append(int(input(f' Quantos gols marcou na {cont}ª partida? ')))
jogador['gols'] = gols[:]
total = sum(gols)
print('='*30)
print(jogador)
print('='*30)
for k, v in jogador.items():
    print(f' O campo {k} tem o valor {v}.')
print('='*30)
print(f' O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
for i, v in enumerate(gols):
    print(f' => Na {i+1}ª partida marcou {v} gols')
