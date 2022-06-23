teste = list()
teste.append('Fábio')
teste.append(58)
print(teste)
dados = list()
dados.append(teste)   #lista dentro de outra lista (junção de listas)
print(dados)
dados.append(teste[:])      #lista dentro de outra lista (cópia)
print(teste)
pessoal = [['Fábio', 58],['Elaine', 48],['José', 11],['Paulo', 15]]
print(pessoal)
print(pessoal[0])
print(pessoal[0][0])
print(pessoal[2][1])

for p in pessoal:
    print(f' {p[0]} tem {p[1]} anos de idade.')
totmai = 0
totmen = 0
for p in pessoal:
    if p[1] < 18:
        print(f' {p[0]} é menor de idade. ')
        totmen += 1
    else:
        print(f' {p[0]} é maior de idade.')
        totmai += 1
print(f' {totmen} são menores de idade e {totmai} são menores.')
