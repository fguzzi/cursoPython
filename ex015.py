km = float(input('Qual a quilometragem rodada? Km '))
dias = int(input('Quantos dias o carro foi utilizado? '))
custo = (km * 0.15) + (dias * 60.00)
print('Para {} dias de uso e {} km rodados, o custo é R$ {:.2f}'.format(dias,km,custo))

# R$ 0.15 por km rodado e R$ 60.00 por dia de uso