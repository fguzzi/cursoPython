s = n = 0
while True:
    n = int(input('Digite um nº: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))


