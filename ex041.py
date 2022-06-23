from datetime import date
print('VERIFICAÇÃO DA CATEGORIA DE UM ATLETA')
nas = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
idade = (atual - nas)
if idade <= 9:
    print('A categoria do atleta de {} anos é MIRIM'.format(idade))
elif idade <= 14:
    print('A categoria do atleta de {} anos é INFANTIL'.format(idade))
elif idade <= 19:
    print('A categoria do atleta de {} anos é JUNIOR'.format(idade))
elif idade <= 25:
    print('A categoria do atleta de {} anos é SENIOR'.format(idade))
else:
    print('A categoria do atleta de {} anos é MASTER'.format(idade))


