vel = float(input('Qual a velocidade atual do carro em km/h? '))
if vel > 80:
    print('MULTADO ! Você excedeu o limite de 80 km/h !')
    multa = (vel - 80) * 7
    print('Você deve pagar a multa no valor de R$ {}'.format(multa))
print('Velocidade dentro do limite ! Tenha uma boa viagem !')
