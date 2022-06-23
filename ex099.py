def maior(num):
    while True:
            if len(num) == 0:
                print('Nenhum valor inserido. O maior é 0.')
                break
            else:
                    maior = num[0]
                    for i in num:
                        if i > maior:
                            maior = i
            print('Analisando os valores passados...')
            print(f' {num} => Foram informados {len(num)} valores ao todo.')
            print(f' O maior valor foi {maior}.')
            break


num = [9, 7, -9, 10, 199, 222, -78, 12]
maior(num)
print('-'*60)
num = [12, 36, 222, -99, 7, 1587]
maior(num)
print('-'*60)
num = [137, 2789]
maior(num)
print('-'*60)
num = [0]
maior(num)
print('-'*60)
num = []
maior(num)
print('-'*60)

