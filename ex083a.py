print('VERIFICAÇÃO DA COLOCAÇÃO DE PARENTESES EM UMA EXPRESSÃO')
expr = (str(input('Digite a expressão: ')))
pab = []
pfch = []
for simb in expr:
    if simb == '(':
        pab.append(simb)
    elif simb == ')':
        pfch.append(simb)
if len(pab) == len(pfch):
    print('A expressão está correta.')
else:
    print('A expressão está errada.')
