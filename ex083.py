print('VERIFICAÇÃO DA COLOCAÇÃO DE PARENTESES EM UMA EXPRESSÃO')
expr = (str(input('Digite a expressão: ')))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão está correta.')
else:
    print('A expressão está errada.')

# A cada 'fecha parêntese' encontrado, o programa exclui um 'abre parêntese'