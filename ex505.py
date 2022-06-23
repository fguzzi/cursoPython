print('ASSOCIAÇÃO ENTRE 3 CAPACITORES')
c1 = 10
print('Capacitor 1: {} microfarads'.format(c1))
c2 = 22
print('Capacitor 2: {} microfarads'.format(c2))
c3 = 6.8
print('Capacitor 3: {} microfarads'.format(c3))
cap_par = c1 + c2 + c3
print('Capacitância para ligação em paralelo é {:.2f} microfarads'.format(cap_par))
cap_ser = (1 / ((1/c1) + (1/c2) + (1/c3)))
print('Capacitância para ligação em série é {:.2f} microfarads'.format(cap_ser))