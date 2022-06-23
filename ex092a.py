from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Digite o nome: '))
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['Ctps'] = int(input('CTPS ( 0 se não tiver): '))
if dados['Ctps'] != 0:
    dados['Contrataçao'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salário R$: '))
    dados['Aposentadoria'] = (dados['Idade'] + (dados['Contrataçao'] + 35) - (datetime.now().year))
print('='*30)
for k, v in dados.items():
    print(f'   -  {k} tem o valor {v}')
