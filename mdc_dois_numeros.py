print('CÁLCULO MDC DE DOIS NÚMEROS')
i = 1
import numpy as np
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
mdc=1
if n1 > n2:
    m = n1
else:
    m= n2
for i in range(1,m):
    if n1 % i == 0 and n2 % i == 0:
        mdc = i
print('O MDC é {}'.format(mdc))
