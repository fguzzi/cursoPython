vel = float(input('Qual a velocidade atual do carro em km/h? '))
if vel > 80:
    print('MULTADO ! Você excedeu o limite de 80 km/h !')
    print('O valor da multa é de R$ {:.2f}'.format((vel - 80) * 7))
else:
    print('Velocidade dentro do limite ! Tenha uma boa viagem !')
