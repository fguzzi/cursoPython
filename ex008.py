metro = float(input('Digite um valor em metros: '))
mm= metro * 1000
cm = metro * 100
dm = metro * 10
dam = metro / 10
hec = metro / 100
km = metro / 1000
print('{:.1f} m é igual a:\n {} mm\n {} cm\n {} dc\n {:.3f} dec\n {:.3f} hec\n {:.4f} km'.format(metro,mm, cm, dm, dam, hec, km))
