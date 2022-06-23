a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
# verificando quem é o menor
menor = a
if b < a and b < c:
      menor = b
if c < a and c < b:
      menor = c
# verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número digitado foi {} e o menor {}'.format(maior, menor))
