from time import sleep
cor = ('\033[m',                 # sem cores
         '\033[0;30;41m',      # vermelho
         '\033[0;30;42m',      # verde
         '\033[0;30;43m',      # amarelo
         '\033[0;30;44m',      # azul
         '\033[0;30;45m',      # roxo
         '\033[0;30')              # branco'

def ajuda(com):
    titulo(f' Acessando o manual do comando \ {com}\' ', 4)
    print(cor[3], end=' ')
    help(com)
    print(cor[0], end=' ')
    sleep(2)

def titulo(msg, c = 0):
    tam = len(msg) + 4
    print(cor[c], end=' ')
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    print(cor[0], end=' ')
    sleep(1)


comando = ' '
while True:
    titulo('SISTEMA DE AJUDA PyHelp', 2)
    comando = str(input('<Função ou Biblioteca> '))
    if comando == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)