#lambda function is similar to Javascript arrow function

_square =   lambda sisi : sisi * sisi

_sisi   =   float(input('Masukkan sisi persegi\n'))
print(f'Luas persegi dengan {_sisi} cm adalah {_square(_sisi)} cm2')