din = float(input('Quanto dinheiro você tem na carteira:  R$ '))
cd = float(input('Digite a cotação do dolar: US$ '))
dolar = din / cd
print('Com  R$ {:.2f}  você poderá comprar até  US$ {:.2f}'.format(din, dolar))
