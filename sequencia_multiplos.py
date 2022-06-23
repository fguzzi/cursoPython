print('SEQUÊNCIA DE MÚLTIPLOS')
i = int(input('Digite o primeiro número da sequência: '))
f = int(input('Digite o último número da sequência: '))
num = int(input('Você deseja os múltiplos de qual número? '))
for c in range(i,f + 1):
    calc = c % num
    if calc == 0:
        print(c, end=' ')
