print('NÚMEROS MULTIPLOS')
a = float(input('Escreva o 1º número: '))
b = float(input('Escreva o 2º número: '))
if a > b and a % b == 0:
    print('O número {} é multiplo de {}'.format(a,b))
elif b > a and b % a == 0:
    print('O número {} é múltiplo de {}'.format(b,a))
elif a == b:
    print('Os números são múltiplos')
else:
    print('Os números não são múltiplos')


#leia dois valores a e b e os escreve com a mensagem: "São múltiplos" ou "Não são múltiplos".