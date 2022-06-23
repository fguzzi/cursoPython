#inserir 5 valores pelo teclado com uso de for
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ' )))
for c, v in enumerate(valores):
    print(f'Na posição {c} temos o valor {v}')

