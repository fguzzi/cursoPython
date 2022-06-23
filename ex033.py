a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceito valor: '))
if a < b and a < c:
    menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('-' * 30)
print('O número maior é {}'.format(maior))
print('O número menor é {}'.format(menor))
