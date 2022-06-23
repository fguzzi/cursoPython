print('TRABALHANDO UM INTERVALO DE 10 NÚMEROS')
maior = 0
menor = 0
pares = 0
impares = 0
somapar = 0
somaimpar = 0
for c in range(1,11):
    num = int(input('Digite o {}º número: '.format(c)))
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
           maior = num
        if num < menor:
            menor = num
for intervalo in range(menor,maior+1):
    if intervalo % 2 == 0:
        somapar = somapar + intervalo
    if intervalo % 2 == 1:
        somaimpar = somaimpar + intervalo

print('A soma dos números pares é {} e dos impares é {}'.format(somapar,somaimpar))
print('O intervalo da sequencia inicia em {} e termina em {}'.format(menor,maior))


## 'Criar um algoritmo em Python que leia os limites inferior e superior
##de um intervalo de 10 números inteiros e apresente todos os números pares no intervalo aberto e seu somatório.
##Suponha que os números digitados são um intervalo crescente.