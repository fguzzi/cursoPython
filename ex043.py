print('\033[4;31mCálculo de IMC\033[m')
peso = float(input('Digite seu peso em Kg: '))
h = float(input('Digite sua altura em m: '))
imc = peso  / (h ** 2)
if imc <18.5:
    print('Com IMC = {:.1f}, você está ABAIXO DO PESO.'.format(imc))
elif 18.5 <= imc < 25:
    print('Com IMC = {:.1f}, você está com PESO IDEAL.'.format(imc))
elif 25 <= imc < 30:
    print('Com IMC = {:.1f}, você está com SOBREPESO.'.format(imc))
elif 30 <= imc < 40:
    print('Com IMC = {:.1f}, você está com OBESIDADE.'.format(imc))
else:
    print('Com IMC = {:.1f}, você está com OBESIDADE MÓRBIDA, cuidado !!!'.format(imc))
