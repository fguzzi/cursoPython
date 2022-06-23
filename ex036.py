print('CÁLCULO DE EMPRÉSTIMO')
casa = float(input('Informe o valor da casa: R$ '))
sal = float(input('Informe seu salário: R$ '))
anos = int(input('Informe em quantos anos quer pagar: '))
minimo = sal * 30 / 100
par = casa / (anos * 12)
print('Para pagar uma casa no valor de R$ {:.2f}, em {} anos,'.format(casa,anos), end=' ')
print('a prestação será de R$ {:.2f}'.format(par))
if par <= minimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO')
