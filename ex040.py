print('CALCULO DE MEDIA')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Com notas {:.1f} e {:.1f} e média {:.1f} você foi REPROVADO'.format(nota1, nota2, media))
elif media >= 5 and media < 7:
    print('Com notas {:.1f} e {:.1f} e média {:.1f} você está em RECUPERAÇÃO'.format(nota1, nota2, media))
elif media >= 7:
    print('Com notas {:.1f} e {:.1f} e média {:.1f} você foi APROVADO'.format(nota1, nota2, media))
