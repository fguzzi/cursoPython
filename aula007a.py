n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva outro número: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
rd = n1 % n2
p = n1 ** n2
print("A soma é {}. \n A subtração é {}, a multiplicação é {}. ".format(s, sub, m), end=" ")
print('A divisão é {:.3f}, a divisão inteira é {}, o resto da divisão é {} e a potenciação é {}'.format(d, di, rd, p))
